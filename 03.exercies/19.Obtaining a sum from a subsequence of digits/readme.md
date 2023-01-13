## Obtaining a sum from a subsequence of digits
Write a program sum_of_digits.py that prompts the user for two natural numbers, say available_digits and desired_sum, and outputs the number of ways of selecting digits from available_digits that sum up to desired_sum. For instance, if available_digits is 12234 and sum is 5 then there are four (4) solutions:

one solution is obtained by selecting 1 and both occurrences of 2 (1+2+2 = 5);

one solution is obtained by selecting 1 and 4 (1+4 = 5);

one solution is obtained by selecting the first occurrence of 2 and 3 (2+3 = 5);

one solution is obtained by selecting the second occurrence of 2 and 3 (2+3 = 5).

Here are possible interactions:

Input a number that we will use as available digits: 12234
Input a number that represents the desired sum: 5
There are 4 solutions.
Input a number that we will use as available digits: 11111
Input a number that represents the desired sum: 5
There is a unique solution.
Input a number that we will use as available digits: 11111
Input a number that represents the desired sum: 6
There is no solution.
Input a number that we will use as available digits: 1234321
Input a number that represents the desired sum: 5
There are 10 solutions. 
Insert your code into sum_of_digits.py

If you are stuck, but only when you are stuck, then use sum_of_digits_scaffold.py