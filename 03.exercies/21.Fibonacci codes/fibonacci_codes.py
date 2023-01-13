'''
Every strictly positive integer N can be uniquely coded as a string sigma
of 0's and 1's ending with 1, so of the form b_2b_3...b_k with k >= 2 and b_k = 1,
such that N is the sum of all F_i's, 2 <= i <= k, with b_i = 1.

Moreover:
- there are no two successive occurrences of 1 in sigma;
- F_k is the largest Fibonacci number that fits in N, and
  if j is the largest integer in {2,...,k-1} such that b_j = 1
  then F_j is the largest Fibonacci number that fits in N - F_k, and
  if i is the largest integer in {2,...,j-1} such that b_i = 1
  then F_i is the largest Fibonacci number that fits in  N - F_k - F_j...

Also, every string of 0's and 1's ending in 1 and having no two
successive occurrences of 1's is a code of a strictly positive integer
according to this coding scheme. For instance:
- There is only one string of 0's and 1's of length 1 ending in 1 and
  having no two successive occurrences of 1's; it is 1, and it codes 1.
- There is only one string of 0's and 1's of length 2 ending in 1 and
  having no two successive occurrences of 1's; it is 01, and it codes 2.
- The strings of 0's and 1's of length 3 ending in 1 and having no two successive occurrences
  of 1's are 001 and 101 and they code 3 and 4, respectively.
- The strings of 0's and 1's of length 4 ending in 1 and having no two successive occurrences
  of 1's are 0001, 1001 and 0101 and they code 5, 6 and 7, respectively.
- The strings of 0's and 1's of length 5 ending in 1 and having no two successive occurrences
  of 1's are 00001, 10001, 01001, 00101 and 10101 and they code 8, 9, 10, 11 and 12, respectively.
- ...

The Fibonacci code of N adds 1 at the end of sigma; the resulting string then ends in two 1's,
therefore marking the end of the code, and allowing one to let one string code a finite sequence
of strictly positive integers. For instance, 00101100111011 codes (11,3,4).
'''


def encode(n):
    '''
    Retuns the Fibonacci code of n, meant to be a strictly positive integer.
    '''
    pass
    # Replace pass above with your code

def decode(code):
    '''
    The argument is meant to be a string of 0's and 1's.
    Returns 0 if the argument cannot be a Fibonacci code;
    otherwise returns the integer argument is the Fibonacci code of.
    '''
    pass
    # Replace pass above with your code

