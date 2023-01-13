# Written by Eric Martin for COMP9021


def balanced_brackets_in(pattern):
    pattern = iter(pattern)
    for symbol in pattern:
        if not symbol.isspace():
            break
    else:
        return True
    brackets = dict(zip('([{', ')]}'))
    if symbol not in brackets:
        for bracket in brackets:
            if symbol == brackets[bracket]:
                return extra_symbols_or_imbalanced(pattern,
                                                   (bracket, brackets[bracket])
                                                  )
        return
    nb_of_opening_brackets = 1
    for c in pattern:
        if c == symbol:
            nb_of_opening_brackets += 1
        elif c == brackets[symbol]:
            if not nb_of_opening_brackets:
                return extra_symbols_or_imbalanced(pattern,
                                                   (symbol, brackets[symbol])
                                                  )
            nb_of_opening_brackets -= 1
        elif not c.isspace():
            return
    return not nb_of_opening_brackets

def extra_symbols_or_imbalanced(pattern, brackets):
    if all(c.isspace() or c in brackets for c in pattern):
        return False
    return
