from copy import deepcopy


def consistently_add_to(mapping, *key_values):
    '''
    >>> D = {}
    >>> consistently_add_to(D, ('A', 1)), D
    (True, {'A': 1})
    >>> consistently_add_to(D, ('A', 1)), D
    (True, {'A': 1})
    >>> consistently_add_to(D, ('A', 2)), D
    (False, {'A': 1})
    >>> consistently_add_to(D, ('B', 2), ('C', 3)), D
    (True, {'A': 1, 'B': 2, 'C': 3})
    >>> consistently_add_to(D, ('A', 1), ('C', 3), ('D', 4)), D
    (True, {'A': 1, 'B': 2, 'C': 3, 'D': 4})
    >>> consistently_add_to(D, ('B', 3), ('E', 5)), D
    (False, {'A': 1, 'B': 2, 'C': 3, 'D': 4})
    '''
    for (key, value) in key_values:
        if mapping.setdefault(key, value) != value:
            return False
    return True


class Expression:
    def __init__(self, root, children=[]):
        self.root = root
        self.children = children

    def __str__(self):
        return self.root if not self.children\
                         else ''.join((self.root, '(',
                                       ', '.join(str(child)
                                                    for child in self.children
                                                ), ')'
                                      )
                                     )

    @classmethod
    def parse_item(_class, expression, parse_subitem=True):
        characters = list(reversed(expression.replace(' ', '')))
        item = _class.parse_subitem(characters)\
                  if parse_subitem\
                  else Atom.parse_subitem_sequence(characters)
        if not item or characters:
            return
        return item

    @classmethod
    def parse_subitem(_class, characters):
        if not characters or not _class.starts_well(characters[-1]):
            return
        symbol = Expression.parse_word(characters)
        if not characters or characters[-1] != '(':
            return _class(symbol)
        characters.pop()
        subitems = Term.parse_subitem_sequence(characters)
        if not subitems or not characters or characters.pop() != ')':
            return
        return _class(symbol, subitems)

    @classmethod
    def parse_subitem_sequence(_class, characters):
        items = []
        while True:
            item = _class.parse_subitem(characters)
            if not item:
                return
            items.append(item)
            if not characters or characters[-1] != ',':
                return items
            characters.pop()

    @staticmethod    
    def parse_word(characters):
        word = [characters.pop()]
        while characters and (characters[-1].isalnum()
                              or characters[-1] == '_'
                             ):
            word.append(characters.pop())
        return ''.join(word)

    @staticmethod
    def fresh_variables(variables, reserved_variables):
        '''
        Returns a dictionary whose keys are the variables that occur both
        in 'variables' and in 'reserved_variables', and whose values
        consist of distinct variables that occur neither in 'variables'
        nor in 'reserved_variables'.
        
        >>> Expression.fresh_variables({'a'}, set())
        {}
        >>> Expression.fresh_variables({'Y'}, {'X'})
        {}
        >>> Expression.fresh_variables({'X'}, {'X'})
        {'X': 'X_0'}
        >>> Expression.fresh_variables({'Y', 'Z'}, {'X', 'Y'})
        {'Y': 'Y_0'}
        >>> Expression.fresh_variables({'U', 'Y', 'Z'}, {'X', 'Y', 'Z'}) ==\
                                                       {'Z': 'Z_0', 'Y': 'Y_0'}
        True
        '''
        substitutions = {}
        # Any variable Var that occurs in both variables and
        # reserved_variables will be renamed to Var_i where i is the
        # least natural number that makes Var_i a new variable (that is,
        # occurring neither in variables nor in reserved_variables nor
        # in the set of variables that have been created so far, if any).
        for variable in variables & reserved_variables:
            i = 0
            while ''.join((variable, '_', str(i))) in variables\
                                                      | reserved_variables:
                i += 1
            substitutions[variable] = ''.join((variable, '_', str(i)))
        return substitutions

    @staticmethod
    def unify_identities(identities):
        assignments = {}
        while identities:
            expression_1, expression_2 = identities.pop()
            if expression_1.root == expression_2.root:
                identities.extend([expr_1, expr_2] for (expr_1, expr_2) in
                                                     zip(expression_1.children,
                                                         expression_2.children
                                                        )
                                 )
            elif expression_1.is_variable():
                # Occurrence check
                # (omitted in most Prolog implementations)
                if expression_1.root in expression_2.variables():
                    return
                assignments[expression_1.root] = expression_2
                for identity in identities:
                    for i in range(2):\
                    identity[i] = identity[i].substitute_in_copy(
                                            {expression_1.root: expression_2}
                                                                )
            elif expression_2.is_variable():
                identities.append([expression_2, expression_1])
            else:
                return
        return assignments

    @staticmethod
    def reduce_substitution(substitution):
        '''
        >>> substitution = {'X': Term.parse_term('Y'),\
                            'Y': Term.parse_term('Z'),\
                            'Z': Term.parse_term('V')\
                           }
        >>> Expression.reduce_substitution(substitution)
        >>> {X: expr.__str__() for (X, expr) in substitution.items()}
        {'X': 'V', 'Y': 'V', 'Z': 'V'}
        '''
        for var in substitution:
            substitution[var] = substitution[var].substitute(substitution)

    def is_variable(self):
        return self.root[0].isupper() or self.root[0] == '_' 

    def variables(self):
        '''
        >>> Term.parse_term('x').variables()
        set()
        >>> Term.parse_term('X').variables()
        {'X'}
        >>> Term.parse_term('f(X, a, X)').variables()
        {'X'}
        >>> Term.parse_term('f(X_0, Y, X_0)').variables() == {'Y', 'X_0'}
        True
        >>> Term.parse_term('f(c, f(X, f(a, Z, b),\
                             f(f(X, Z, U), a, T)), f(a, U, a))'\
                           ).variables() == {'U', 'T', 'X', 'Z'}
        True
        '''
        variables = {self.root} if self.is_variable() else set()
        variables.update(*(child.variables() for child in self.children))
        return variables

    def individualise_underscores(self, variables=None, index=-1):
        '''
        >>> term = Term.parse_term('f(g(h(a, _), X), _2, h(a, _), _)')
        >>> term.individualise_underscores()
        3
        >>> print(term)
        f(g(h(a, _0), X), _2, h(a, _1), _3)
        '''
        if variables is None:
            variables = self.variables()
        if self.root == '_':
            while True:
                index += 1
                next_underscore = '_' + str(index)
                if next_underscore not in variables:
                    self.root = next_underscore
                    return index
        if not self.children:
            return index
        for child in self.children:
            index = child.individualise_underscores(variables, index)
        return index

    def rename_variables(self, substitution):
        '''
        >>> atom = Atom.parse_atom('join(l(H, T),X, l(H, Y))')
        >>> print(atom.rename_variables({'X': 'A', 'Y': 'B', 'Z': 'C'}))
        join(l(H, T), A, l(H, B))
        '''
        return deepcopy(self)._rename_variables(substitution)

    def _rename_variables(self, substitution):
        if self.is_variable():
            if self.root in substitution:
                self.root = substitution[self.root]
        else:
            for child in self.children:
                child._rename_variables(substitution)
        return self
        
    def substitute_in_copy(self, substitution):
        '''
        Applies 'substitution' to 'term' until it is not possible to
        apply it any more. Would loop for some substitutions, e.g,
        {'X': 'X'}, but not for unifiers.
        
        >>> term = Term.parse_term('f(a, X, g(Y, b), h(h(h(Z))))')
        >>> print(term.substitute_in_copy({'X': Term.parse_term('X_0'),\
                                           'Z': Term.parse_term('Z_0')\
                                          }\
                                         )\
                 )
        f(a, X_0, g(Y, b), h(h(h(Z_0))))
        >>> term = Term.parse_term('h(h(f(U, Y, g(Z, Z))))')
        >>> print(term.substitute_in_copy({'Z': Term.parse_term('ZZZ')}))
        h(h(f(U, Y, g(ZZZ, ZZZ))))
        >>> term = Term.parse_term('f(a, X, g(Y, b), h(h(h(Z))))')
        >>> print(term.substitute_in_copy({'X_0' : Term.parse_term('h(Z_0)'),\
                                           'X': Term.parse_term('X_0'),\
                                           'Z_0': Term.parse_term('c')\
                                          }\
                                         )\
                 )
        f(a, h(c), g(Y, b), h(h(h(Z))))
        '''
        return deepcopy(self).substitute(substitution)

    def substitute(self, substitution):
        if self.is_variable():
            if self.root in substitution:
                self.root, self.children = substitution[self.root].root,\
                                           substitution[self.root].children
                self.substitute(substitution)
        else:
            for child in self.children:
                child.substitute(substitution)
        return self
            
    def unify(self, expression):
        '''
        Returns a most general unifier with 'expression' if one exists,
        in the form of a dictionnary whose keys are variables and whose
        values are the terms that should be substituted for the
        associated variables; otherwise returns False.
        
        >>> term_1 = Term.parse_term('X')
        >>> term_2 = Term.parse_term('X')
        >>> unifier = {X: str(expr)\
                           for (X, expr) in term_1.unify(term_2).items()\
                      }
        >>> unifier == {}
        True
        >>> term_1 = Term.parse_term('X')
        >>> term_2 = Term.parse_term('a')
        >>> unifier = {X: str(expr)\
                           for (X, expr) in term_1.unify(term_2).items()\
                      }
        >>> unifier == {'X': 'a'}
        True
        >>> term_1 = Term.parse_term('X')
        >>> term_2 = Term.parse_term('Y')
        >>> unifier = {X: str(expr)\
                           for (X, expr) in term_1.unify(term_2).items()\
                      }
        >>> unifier == {'X': 'Y'} or unifier == {'Y': 'X'}
        True
        >>> term_1 = Term.parse_term('f(X, Y)')
        >>> term_2 = Term.parse_term('f(Y, X)')
        >>> unifier = {X: str(expr)\
                           for (X, expr) in term_1.unify(term_2).items()\
                      }
        >>> unifier == {'X': 'Y'} or unifier == {'Y': 'X'}
        True
        >>> term_1 = Term.parse_term('f(X1, h(X1), X2)')
        >>> term_2 = Term.parse_term('f(g(X3), X4, X3)')
        >>> unifier = {X: str(expr)\
                           for (X, expr) in term_1.unify(term_2).items()\
                      }
        >>> unifier == {'X4': 'h(X1)', 'X2': 'X3', 'X1': 'g(X3)'}\
            or unifier == {'X4': 'h(g(X3))', 'X2': 'X3', 'X1': 'g(X3)'}
        True
        >>> term_1 = Term.parse_term('f(X1 ,g(X2, X3), X2, b)')
        >>> term_2 = Term.parse_term('f(g(h(a, X5), X2), X1, h(a, X4), X4)')
        >>> unifier = term_1.unify(term_2)
        >>> Expression.reduce_substitution(unifier)
        >>> {X: str(expr) for (X, expr) in unifier.items() } ==\
                      {'X3': 'h(a, b)', 'X1': 'g(h(a, b), h(a, b))',\
                       'X4': 'b', 'X5': 'b', 'X2': 'h(a, b)'\
                      }
        True
        >>> term_1 = Term.parse_term('f(X, Y, U)')
        >>> term_2 = Term.parse_term('f(Y, U, g(X))')
        >>> term_1.unify(term_2)
        '''
        return Expression.unify_identities([[self, expression]])


class Term(Expression):
    class TermError(Exception):
        pass

    def __init__(self, root, children=[]):
        super().__init__(root, children)
        self.function_symbols = {} if self.is_variable()\
                                   else {root: len(self.children)}
        for child in self.children:
            if not consistently_add_to(self.function_symbols,
                                       *child.function_symbols.items()
                                      ):
                raise Term.TermError('Function symbol used with different '
                                     f'arities in {self}'
                                    )

    @staticmethod
    def starts_well(c):
        return c.isidentifier()
                                  
    @staticmethod
    def parse_term(expression):
        '''
        >>> term = Term.parse_term('X')
        >>> print(term)
        X
        >>> term.function_symbols
        {}
        >>> term = Term.parse_term('bob')
        >>> print(term)
        bob
        >>> term.function_symbols
        {'bob': 0}
        >>> term = Term.parse_term('father(bob, sandra)')
        >>> print(term)
        father(bob, sandra)
        >>> term.function_symbols == {'father': 2, 'bob': 0, 'sandra': 0}
        True
        >>> term = Term.parse_term('l(e, l(H, T))')
        >>> print(term)
        l(e, l(H, T))
        >>> term.function_symbols == {'l': 2, 'e': 0}
        True
        >>> Term.parse_term('2')
        Traceback (most recent call last):
        ...
        Term.TermError: 2 is syntactically incorrect
        >>> Term.parse_term('father(bob, sandra))')
        Traceback (most recent call last):
        ...
        Term.TermError: father(bob, sandra)) is syntactically incorrect
        >>> Term.parse_term('father(bob, , sandra)')
        Traceback (most recent call last):
        ...
        Term.TermError: father(bob, , sandra) is syntactically incorrect
        >>> Term.parse_term('father(bob, father(sandra, john, mary))')
        Traceback (most recent call last):
        ...
        Term.TermError: Function symbol used with different arities in \
father(bob, father(sandra, john, mary))
        '''
        term = Term.parse_item(expression)
        if not term:
            raise Term.TermError(f'{expression} is syntactically incorrect')
        return term


class Atom(Expression):
    class AtomError(Exception):
        pass

    def __init__(self, root, children=[]):
        super().__init__(root, children)
        self.function_symbols = {}
        for child in self.children:
            if not consistently_add_to(self.function_symbols,
                                       *child.function_symbols.items()
                                      ):
                raise Term.TermError('Function symbol used with different '
                                     f'arities in {self}'
                                    )
        if self.root in self.function_symbols:
            raise Atom.AtomError('Predicate symbol also function symbol '
                                 f'in {self}'
                                )

    @staticmethod
    def starts_well(c):
        return c.islower()

    @staticmethod
    def parse_atom(expression):
        '''
        >>> atom = Atom.parse_atom('bob')
        >>> print(atom)
        bob
        >>> atom.function_symbols
        {}
        >>> atom = Atom.parse_atom('father(bob, sandra)')
        >>> print(atom)
        father(bob, sandra)
        >>> atom.function_symbols == {'bob': 0, 'sandra': 0}
        True
        >>> atom = Atom.parse_atom('join(l(H, T), X, l(H, Y))')
        >>> print(atom)
        join(l(H, T), X, l(H, Y))
        >>> atom.function_symbols
        {'l': 2}
        >>> Atom.parse_atom('X')
        Traceback (most recent call last):
        ...
        Atom.AtomError: X is syntactically incorrect
        >>> Atom.parse_atom('l(e, l(H, T))')
        Traceback (most recent call last):
        ...
        Atom.AtomError: Predicate symbol also function symbol in l(e, l(H, T))
        '''
        atom = Atom.parse_item(expression)
        if not atom:
            raise Atom.AtomError(f'{expression} is syntactically incorrect')
        return atom


if __name__ == '__main__':
    import doctest
    doctest.testmod()
