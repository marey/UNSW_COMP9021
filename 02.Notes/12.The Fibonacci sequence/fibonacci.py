# COMP9021 Term 3 2021


'''
Computes the (n+1)st Fibonacci number iteratively and recursively,
with and without memoisation.
'''


from math import sqrt


def fibonacci_sequence():
    '''
    >>> S = fibonacci_sequence()
    >>> list(next(S) for _ in range(20))
    [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, \
2584, 4181]
    '''
    yield 0
    yield 1
    previous, current = 0, 1
    while True:
        previous, current = current, previous + current
        yield current

def iterative_fibonacci(n):
    '''
    >>> [iterative_fibonacci(n) for n in range(20)]
    [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, \
2584, 4181]
    '''
    if n < 2:
        return n
    previous, current = 0, 1
    for _ in range(2, n + 1):
        previous, current = current, previous + current
    return current

def recursive_fibonacci(n):
    '''
    >>> [recursive_fibonacci(n) for n in range(20)]
    [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, \
2584, 4181]
    '''
    if n >= 2:
        return recursive_fibonacci(n - 2) + recursive_fibonacci(n - 1)
    return n

def memoise_fibonacci(n, fibonacci={0: 0, 1: 1}):
    '''
    >>> [memoise_fibonacci(n) for n in range(20)]
    [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, \
2584, 4181]
    '''
    if n not in fibonacci:
        fibonacci[n] = memoise_fibonacci(n - 1) + memoise_fibonacci(n - 2)
    return fibonacci[n]

def closed_form_fibonacci(n):
    '''
    >>> [closed_form_fibonacci(n) for n in range(20)]
    [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, \
2584, 4181]
    '''
    sqrt_5 = sqrt(5)
    return round(1 / sqrt_5 * ((1 + sqrt_5) / 2) ** n)


if __name__ == '__main__':
    import doctest
    doctest.testmod()
