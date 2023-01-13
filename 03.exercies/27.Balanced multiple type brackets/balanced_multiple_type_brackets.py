# Written by Eric Martin for COMP9021


def balanced_brackets_in(pattern):
    pattern = iter(pattern)
    for c in pattern:
        if not c.isspace():
            break
    else:
        return True
    brackets = dict(zip('([{', ')]}')) 
    stack = []
    while True:
        if c in brackets:
            stack.append(brackets[c])
        elif c in brackets.values():
            try:
                if stack.pop() != c:
                    raise IndexError
            except IndexError:
                if all(c.isspace() or c in brackets or c in brackets.values()
                           for c in pattern
                      ):
                    return False
                return
        elif not c.isspace():
            return
        try:
            c = next(pattern)
        except StopIteration:
            return not stack
