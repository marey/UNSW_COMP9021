#  Written by Eric Martin for COMP9021


from functools import partial
from operator import add, mul, sub, truediv
from math import isnan


additive_operators = {'+': add, '-': sub}
multiplicative_operators = {'*': mul, '/': truediv}

def evaluate(expression):
    if any(not (c.isdigit() or c.isspace() or c in '()+-*/')
               for c in expression
          ):
        return
    tokens = [c for c in expression if not c.isspace()]
    tokens.reverse()
    value = evaluate_expression_or_term(additive_operators, tokens)
    if tokens or value is None:
        return
    if isnan(value):
        raise ZeroDivisionError
    return value

def evaluate_expression_or_term(operators, tokens):
    evaluation_function = partial(evaluate_expression_or_term,
                                  multiplicative_operators
                                 ) if '+' in operators\
                                   else evaluate_factor
    value = evaluation_function(tokens)
    if value is None:
        return
    while tokens and tokens[-1] in operators:
        operator = tokens.pop()
        other_value = evaluation_function(tokens)
        if other_value is None:
            return
        try:
            value = operators[operator](value, other_value)
        except ZeroDivisionError:
            value = float('nan')
    return value

def evaluate_factor(tokens):
    if not tokens:
        return
    token = tokens.pop()
    if token == '(':
        value = evaluate_expression_or_term(additive_operators, tokens)
        if value is None or not tokens or tokens.pop() != ')':
            return
        return value
    if token.isdigit():
        return evaluate_number(int(token), tokens)
    
def evaluate_number(digit, tokens):
    number = digit
    while tokens and tokens[-1].isdigit():
        number = number * 10 + int(tokens.pop())
    return number
