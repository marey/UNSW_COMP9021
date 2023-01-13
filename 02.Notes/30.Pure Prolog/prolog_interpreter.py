# COMP9021 Term 3 2021


'''
A Prolog interpreter for definite logic programs.
Illustrates the use of a deque for depth-first and breadth-first search
for a solution.

'''


from collections import deque
from itertools import islice

from logic import *


class Conjunction(list):
    class ConjunctionError(Exception):
        pass

    def __init__(self, conjuncts=[]):
        super().__init__(conjuncts)
        self.predicate_symbols = {}
        self.function_symbols = {}
        if not consistently_add_to(self.predicate_symbols, 
                                   *((atom.root, len(atom.children))
                                        for atom in self
                                    )
                                  ):
            raise Conjunction.ConjunctionError('Predicate symbol used with '
                                               f'different arities in {self}'
                                              )
        for atom in self:
            if not consistently_add_to(self.function_symbols,
                                       *atom.function_symbols.items()
                                      ):
                raise Conjunction.ConjunctionError('Function symbol used with '
                                                   'different arities in '
                                                   f'{self}'
                                                  )
        if self.predicate_symbols.keys() & self.function_symbols.keys():
            raise Conjunction.ConjunctionError('Predicate symbol also '
                                               f'function symbol in {self}'
                                              )

    def __str__(self):
        return ', '.join(str(atom) for atom in self)

    @staticmethod
    def parse_conjunction(expression):
        '''
        >>> conjunction = Conjunction.parse_conjunction('father')
        >>> print(conjunction)
        father
        >>> conjunction.predicate_symbols
        {'father': 0}
        >>> conjunction.function_symbols
        {}
        >>> conjunction = \
Conjunction.parse_conjunction('male(X), parent(Z, X), parent(Z, Y)')
        >>> print(conjunction)
        male(X), parent(Z, X), parent(Z, Y)
        >>> conjunction.predicate_symbols == {'male': 1, 'parent': 2}
        True
        >>> conjunction.function_symbols
        {}
        >>> conjunction = Conjunction.parse_conjunction('reduce(X, '\
'add(mult(N, x), M1)), reduce(Y, add(mult(o, x), M2)), plus(M1, M2, M)')
        >>> print(conjunction)
        reduce(X, add(mult(N, x), M1)), reduce(Y, add(mult(o, x), M2)), \
plus(M1, M2, M)
        >>> conjunction.predicate_symbols == {'reduce': 2, 'plus': 3}
        True
        >>> conjunction.function_symbols ==\
{'add': 2, 'mult': 2, 'x': 0, 'o': 0}
        True
        >>> Conjunction.parse_conjunction('plus(X, Y, U), plus(times(U, Y, Z)')
        Traceback (most recent call last):
        ...
        Conjunction.ConjunctionError: plus(X, Y, U), plus(times(U, Y, Z) \
is syntactically incorrect
        >>> Conjunction.parse_conjunction('male(X), parent(Z, X), '\
'parent(male(Z), Y)')
        Traceback (most recent call last):
        ...
        Conjunction.ConjunctionError: Predicate symbol also function symbol \
in male(X), parent(Z, X), parent(male(Z), Y)
        '''
        if expression.isspace():
            return Conjunction()
        conjunction = Expression.parse_item(expression, parse_subitem=False)
        if not conjunction:
            raise Conjunction.ConjunctionError(f'{expression} is '
                                               'syntactically incorrect'
                                              )
        return Conjunction(conjunction)


class Rule:
    class RuleError(Exception):
        pass

    def __init__(self, head, body=Conjunction()):
        self.head = head
        self.body = body
        self.variables =  self.head.variables()
        self.variables.update(*(atom.variables() for atom in self.body))
        if not self.body:
            return
        if not consistently_add_to({self.head.root: len(self.head.children)}, 
                                   *self.body.predicate_symbols.items()
                                  ):
            raise Rule.RuleError("Head's predicate symbol used with "
                                 f'different arities in {self}'
                                )
        if not consistently_add_to(self.head.function_symbols, 
                                   *self.body.function_symbols.items()
                                  ):
            raise Rule.RuleError('Function symbol used with different '
                                 f'arities in head and body of {self}'
                                )
        if self.head.root in self.body.function_symbols:
            raise Rule.RuleError('Predicate symbol in head also '
                                 f'function symbol in body of {self}'
                                )
        if self.head.function_symbols.keys()\
           & self.body.predicate_symbols.keys():
            raise Rule.RuleError('Function symbol in head also '
                                 f'predicate symbol in body of {self}'
                                )

    def __str__(self):
        if not self.body:
            return str(self.head) + '.'
        return ' :- '.join((str(self.head),
                            ', '.join(str(atom) for atom in self.body)
                           )
                          ) + '.'

    @staticmethod
    def parse_rule(expression):
        '''
        >>> rule = Rule.parse_rule('female(alice).')
        >>> print(rule)
        female(alice).
        >>> rule.variables
        set()
        >>> rule = Rule.parse_rule('sisterof(X, Y)  :-  parents(X, M, F), '\
'female(X), parents(Y, M, F).')
        >>> print(rule)
        sisterof(X, Y) :- parents(X, M, F), female(X), parents(Y, M, F).
        >>> rule.variables == {'F', 'M', 'X', 'Y'}
        True
        >>> Rule.parse_rule('female(alice)')
        Traceback (most recent call last):
        ...
        Rule.RuleError: female(alice) does not end in a full stop
        >>> Rule.parse_rule(' :- female(alice).')
        Traceback (most recent call last):
        ...
        logic.Atom.AtomError:   is syntactically incorrect
        >>> Rule.parse_rule(' female(alice) :- .')
        Traceback (most recent call last):
        ...
        Rule.RuleError:  female(alice) :- . is syntactically invalid
        >>> Rule.parse_rule('sisterof(X, Y)  :-  parents(X, M, F), '\
'sisterof(X), parents(Y, M, F).')
        Traceback (most recent call last):
        ...
        Rule.RuleError: Head's predicate symbol used with different arities \
in sisterof(X, Y) :- parents(X, M, F), sisterof(X), parents(Y, M, F).
        >>> Rule.parse_rule('times(s(X), Y, Z) :- plus(X, Y, U), '\
'minus(times(U, Y, Z)).')
        Traceback (most recent call last):
        ...
        Rule.RuleError: Predicate symbol in head also function symbol in \
body of times(s(X), Y, Z) :- plus(X, Y, U), minus(times(U, Y, Z)).
        '''
        if expression[-1] != '.':
            raise Rule.RuleError(f'{expression} does not end in a full stop')
        rule = expression[: -1].split(':-')
        if len(rule) < 1 or len(rule) > 2 or\
           len(rule) == 2 and rule[1].isspace():
            raise Rule.RuleError(f'{expression} is syntactically invalid')
        head = Atom.parse_atom(rule[0])
        if len(rule) == 1:
            return Rule(head)
        return Rule(head, Conjunction.parse_conjunction(rule[1]))


class LogicProgram:
    class LogicProgramError(Exception): 
        pass

    class QueryError(Exception):
        pass

    def __init__(self, filename):
        self.program = []
        self.predicate_symbols = {}
        self.function_symbols = {}
        rule_nb = 0
        with open(filename) as file:
            for rule in file:
                rule = rule.strip()
                if not rule or rule.startswith('%'):
                    continue
                rule = Rule.parse_rule(rule)
                rule_nb += 1
                if not consistently_add_to(self.predicate_symbols,
                                           (rule.head.root,
                                            len(rule.head.children)
                                           ),
                                           *rule.body.predicate_symbols.items()
                                          ):
                    raise LogicProgram.LogicProgramError(
                                'Predicate symbol used with different arities '
                                f'in rule nb {rule_nb} and in previous rules'
                                                        )
                if not consistently_add_to(self.function_symbols,
                                           *rule.head.function_symbols.items(),                                           
                                           *rule.body.function_symbols.items()
                                          ):
                    raise LogicProgram.LogicProgramError(
                                'Function symbol used with different arities '
                                f'in rule nb {rule_nb} and in previous rules'
                                                        )
                if self.predicate_symbols.keys()\
                   & self.function_symbols.keys():
                    raise LogicProgram.LogicProgramError(
                          'Symbol used as both predicate and function symbols '
                          f'in rule nb {rule_nb} and in previous rules'
                                                        )
                underscore_index =\
                        rule.head.individualise_underscores(rule.variables)
                for atom in rule.body:
                    underscore_index =\
                            atom.individualise_underscores(rule.variables,
                                                           underscore_index
                                                          )
                self.program.append(rule)

    def solve(self, query, depth_first=True):
        query = Conjunction.parse_conjunction(query)
        if any(predicate_symbol not in self.predicate_symbols
               or query.predicate_symbols[predicate_symbol]
                  != self.predicate_symbols[predicate_symbol]
                      for predicate_symbol in query.predicate_symbols
              ):
            raise LogicProgram.QueryError(f'Predicate symbol in {query} '
                                          'not in program'
                                         )
        if any(function_symbol not in self.function_symbols
               or query.function_symbols[function_symbol]
                  != self.function_symbols[function_symbol]
                      for function_symbol in query.function_symbols
              ):
            raise LogicProgram.QueryError(f'Function symbol in {query} '
                                           'not in program'
                                          )               
        query_variables = {var for atom in query for var in atom.variables()}
        # A list of pairs consisting of:
        # - a list of goals to be solved, and
        # - the substitution to apply to the variables that occur in the
        #   query as determined by the unifications computed so far.
        goals_solution_pairs = deque([(deque(query),
                                       {var: Term(var)
                                            for var in query_variables
                                       }
                                      )
                                     ]
                                    )
        while goals_solution_pairs:
            goals, solution = goals_solution_pairs.popleft()
            if not goals:
                yield {var: str(solution[var]) for var in solution}
                continue
            reserved_variables = query_variables\
                                 | {var for atom in goals
                                           for var in atom.variables()
                                   }
            goal = goals.popleft()
            next_goals_solution_pairs = deque()
            for rule in self.program:
                variable_renaming =\
                        Expression.fresh_variables(rule.variables,
                                                   reserved_variables
                                                  )
                head = rule.head.rename_variables(variable_renaming)
                mgu = goal.unify(head)
                if mgu is not None:
                    new_goals = deque(atom.rename_variables(variable_renaming)
                                         .substitute(mgu) for atom in rule.body
                                     )
                    new_goals.extend(goal.substitute_in_copy(mgu)
                                          for goal in goals
                                    )
                    next_goals_solution_pairs.append(
                                   (new_goals,
                                    {var: solution[var].substitute_in_copy(mgu)
                                         for var in solution
                                    }
                                   )
                                                    )
            if depth_first:
                goals_solution_pairs.extendleft(
                                        reversed(next_goals_solution_pairs)
                                               )
            else:
                goals_solution_pairs.extend(next_goals_solution_pairs)


if __name__ == '__main__':
    import doctest
    doctest.testmod()

    print('TESTING DEPTH FIRST')
    LP = LogicProgram('prolog_ex_1.pl')
    print('A few queries for prolog_ex_1.pl')
    print('  Solutions to father(X, jack):')
    for solution in LP.solve('father(X, jack)'):
        print('   ', solution)
    print('  Solutions to grandparent(john, X):')
    for solution in LP.solve('grandparent(john, X)'):
        print('   ', solution)
    print()

    LP = LogicProgram('prolog_ex_3.pl')
    print('A query for prolog_ex_3.pl')
    print('  Solutions to relation(f(f(f(g(f(a))))), f(f(g(g(a)))), X):')
    for solution in LP.solve('relation(f(f(f(g(f(a))))), f(f(g(g(a)))), X)'):
        print('   ', solution)
    print()

    print('TESTING BREADTH FIRST')
    LP = LogicProgram('prolog_ex_1.pl')
    print('A few queries for prolog_ex_1.pl')
    print('  Solutions to father(X, jack):')
    for solution in LP.solve('father(X, jack)', False):
        print('   ', solution)
    print('  Solutions to grandparent(john, X):')
    for solution in LP.solve('grandparent(john, X)', False):
        print('   ', solution)
    print()

    LP = LogicProgram('prolog_ex_2.pl')
    print('A query for prolog_ex_2.pl')
    print('  Solutions to join(X, X, Y):')
    for solution in islice(LP.solve('join(X, X, Y)'), 3):
        print('   ', solution)
    print()

    LP = LogicProgram('prolog_ex_3.pl')
    print('A query for prolog_ex_3.pl')
    print('  Solutions to relation(f(f(f(g(f(a))))), f(f(g(g(a)))), X):')
    for solution in LP.solve('relation(f(f(f(g(f(a))))), f(f(g(g(a)))), X)',\
                             False\
                            ):
        print('   ', solution)

    

