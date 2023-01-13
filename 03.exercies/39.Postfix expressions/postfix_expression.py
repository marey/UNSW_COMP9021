# Written by Eric Martin for COMP9021


from operator import add, sub, mul, floordiv

def evaluate(expression):
    operators = {'+': add, '-': sub, '*': mul, '/': floordiv}
    stack = []
    processing_number = False
    for c in expression:
        if c.isspace():
            processing_number = False
        elif c.isdigit():
            if not processing_number:
                stack.append(int(c))
                processing_number = True
            elif stack[-1]:
                stack[-1] = stack[-1] * 10 + int(c)
            else:
                return
        elif c in operators:
            try:
                operand_2 = stack.pop()
                stack[-1] = operators[c](stack[-1], operand_2)
            except IndexError:
                return
            except ZeroDivisionError:
                if not stack[-1]:
                    stack[-1] = float('nan')
                elif stack[-1] > 0:
                    stack[-1] = float('inf')
                else:
                    stack[-1] = float('-inf')
            processing_number = False
        else:
            return
    if len(stack) != 1:
        return
    return stack[-1]
