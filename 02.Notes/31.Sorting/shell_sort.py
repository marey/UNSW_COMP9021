# Written by Eric Martin for COMP9021


from random import shuffle


def shell_sort(L):
    '''
    >>> L = []
    >>> shell_sort(L)
    >>> L
    []
    >>> L = [0]
    >>> shell_sort(L)
    >>> L
    [0]
    >>> L = [0, 1]
    >>> shell_sort(L)
    >>> L
    [0, 1]
    >>> L = [1, 0]
    >>> shell_sort(L)
    >>> L
    [0, 1]
    >>> L = list(range(8))
    >>> shell_sort(L)
    >>> L
    [0, 1, 2, 3, 4, 5, 6, 7]
    >>> L.reverse()
    >>> shell_sort(L)
    >>> L    
    [0, 1, 2, 3, 4, 5, 6, 7]
    >>> shuffle(L)
    >>> shell_sort(L)
    >>> L    
    [0, 1, 2, 3, 4, 5, 6, 7]
    '''
    for h in range(len(L) - 1, 0, -1):
        # We use Pratt's method which uses as gaps all numbers of the form
        # 2^i * 3^j
        p = h
        while p % 2 == 0:
            p //= 2
        while p % 3 == 0:
            p //= 3
        if p != 1:
            continue
        for i in range(len(L) - h):
            if L[i + h] < L[i]:
                L[i + h], L[i] = L[i], L[i + h]


if __name__ == '__main__':
    import doctest
    doctest.testmod()
