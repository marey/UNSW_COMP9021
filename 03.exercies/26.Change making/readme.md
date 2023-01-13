Write a program change_making.py that prompts the user for the face values of coins and their associated quantities as well as for an amount, and if possible, outputs the minimal number of coins needed to match that amount, as well as the detail of how many coins of each type value are used.

The face values and associated quantities should be input as a dictionary. You might find the literal_eval() function from the ast module to be useful.

A solution is output from smallest face value to largest face value. If a solution is represented as a list of pairs of the form (coin face value, number of coins) ordered from smallest to largest face value, then the solutions themselves are output in lexicographical order (for sequences of pairs). All face values for a given solution are right aligned.

Insert your code into change_making.py.

Here are examples of interactions:

$ python3 change_making.py
Input a dictionary whose keys represent coin face values
with as value for a given key the number of coins
that are available for the corresponding face value:
    {2: 100, 50: 100}
Input the desired amount: 99

There is no solution.

$ python3 change_making.py
Input a dictionary whose keys represent coin face values
with as value for a given key the number of coins 
that are available for the corresponding face value:
    {1: 30, 20: 30, 50: 30}
Input the desired amount: 60

There is a unique solution:
$20: 3

$ python3 change_making.py
Input a dictionary whose keys represent coin face values
with as value for a given key the number of coins
that are available for the corresponding face value:
    {1: 100, 2: 5, 3: 4, 10: 5, 20: 4, 30: 1}
Input the desired amount: 107

There are 2 solutions:
$1: 1
$3: 2
$10: 1
$20: 3
$30: 1

$2: 2
$3: 1
$10: 1
$20: 3
$30: 1

$ python3 change_making.py
Input a dictionary whose keys represent coins face values
with as value for a given key the number of coins
that are available for the corresponding face value:
    {1: 7, 2: 5, 3: 4, 4: 3, 5: 2}
Input the desired amount: 29

There are 4 solutions:
$1: 1
$3: 2
$4: 3
$5: 2

$2: 1
$3: 3
$4: 2
$5: 2

$2: 2
$3: 1
$4: 3
$5: 2

$3: 4
$4: 3
$5: 1

$ python3 change_making.py
Input a dictionary whose keys represent coins face values
with as value for a given key the number of coins 
that are available for the corresponding face value:
    {11:34, 12:34, 13: 234, 17:44, 18:54, 19: 3}
Input the desired amount: 3422

There are 8 solutions:
$11: 1
$12: 4
$13: 122
$17: 44
$18: 54
$19: 3

$11: 1
$13: 127
$17: 43
$18: 54
$19: 3

$11: 2
$12: 2
$13: 123
$17: 44
$18: 54
$19: 3

$11: 3
$13: 124
$17: 44
$18: 54
$19: 3

$12: 1
$13: 127
$17: 44
$18: 53
$19: 3

$12: 2
$13: 126
$17: 43
$18: 54
$19: 3

$12: 6
$13: 121
$17: 44
$18: 54
$19: 3

$13: 128
$17: 44
$18: 54
$19: 2


The natural approach makes use of the linear programming technique exemplified in the computation of the Levenshtein distance between two words discussed in this week's lecture.