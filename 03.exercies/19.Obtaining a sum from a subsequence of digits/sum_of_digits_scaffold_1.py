import sys


def solve(digits, desired_sum):
    if desired_sum < 0:
        pass
        # Replace pass above with your code
        return 0
    if digits == 0:
        pass
        # Replace pass above with your code
    # Either take the last digit d from digits and try to
    # get desired_sum - d from the remaining digits, or do not take
    # the last digit and try to get desired_sum from the remaining
    # digits.
    #
    # Insert code here

try:
    digits = int(input('Input a natural number for the available digits: '))
    if digits < 0:
        raise ValueError
except ValueError:
    print('Incorrect input, giving up.')
    sys.exit()
try:
    desired_sum = int(input('Input a natural number for the desired sum: '))
    if desired_sum < 0:
        raise ValueError
except ValueError:
    print('Incorrect input, giving up.')
    sys.exit()
nb_of_solutions = solve(digits, desired_sum)
if nb_of_solutions == 0:
    print('There is no solution.')
elif nb_of_solutions == 1:
    print('There is a unique solution.')
else:
    print('There are', nb_of_solutions, 'solutions.')

