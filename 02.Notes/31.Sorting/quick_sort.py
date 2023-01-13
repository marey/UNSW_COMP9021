# Written by Eric Martin for COMP9021


from random import shuffle


def quick_sort(L):
    '''
    >>> L = []
    >>> quick_sort(L)
    >>> L
    []
    >>> L = [0]
    >>> quick_sort(L)
    >>> L
    [0]
    >>> L = [0, 1]
    >>> quick_sort(L)
    >>> L
    [0, 1]
    >>> L = [1, 0]
    >>> quick_sort(L)
    >>> L
    [0, 1]
    >>> L = list(range(8))
    >>> quick_sort(L)
    >>> L
    [0, 1, 2, 3, 4, 5, 6, 7]
    >>> L.reverse()
    >>> quick_sort(L)
    >>> L    
    [0, 1, 2, 3, 4, 5, 6, 7]
    >>> shuffle(L)
    >>> quick_sort(L)
    >>> L    
    [0, 1, 2, 3, 4, 5, 6, 7]
    '''
    quicksort(L, 0, len(L) - 1)

def quicksort(L, start, last):
    if last - start < 1:
        return
    split_point = partition(L, start, last)
    quicksort(L, start, split_point - 1)
    quicksort(L, split_point + 1, last)

def partition(L, start, end):
    pivot_value = L[start]
    left_mark = start + 1
    right_mark = end
    while True:
        while left_mark <= right_mark and L[left_mark] <= pivot_value:
            left_mark += 1
        while right_mark > left_mark and L[right_mark] >= pivot_value:
            right_mark -= 1
        # All values till position left_mark excluded are
        # at most equal to the pivot.
        # All values from position right_mark excluded are
        # at least equal to the pivot.
        # The value at position right_mark is greater than the pivot.
        if left_mark == right_mark:
            right_mark -= 1
        if right_mark == start:
            return start
        # Either the penultimate if statement was true
        # and its body has been executed, or two values
        # next to each other have just been swapped.
        if left_mark == right_mark + 1:
            L[start], L[right_mark] = L[right_mark], L[start]
            return right_mark
        L[left_mark], L[right_mark] = L[right_mark], L[left_mark]


if __name__ == '__main__':
    import doctest
    doctest.testmod()
