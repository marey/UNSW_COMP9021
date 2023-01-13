Write a program that prints out the decimal value of a Roman numeral.

Your program should accept the Roman numeral from the command line arguments. You may assume the Roman numeral is in the "standard" form, i.e., any digits involving 4 and 9 will always appear in the subtractive form.

Sample interactions
python roman_numerals.py II
2
python roman_numerals.py IV
4
python roman_numerals.py IX
9
python roman_numerals.py XIX
19
python roman_numerals.py XX
20
python roman_numerals.py MDCCLXXVI
1776
python roman_numerals.py MMXIX
2019
Hints:

Use a loop to iterate through the Roman numeral to figure out their value.

Use a list of tuples to store the string characters and their respective values, compare the characters from the input to this list.

Use a while loop so you can manually control the indices.