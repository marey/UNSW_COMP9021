Write a program that prompts the user for an amount, and outputs the minimal number of coins needed to yield that amount, as well as the detail of how many coins of each value are used. The available coins have a face value which is one of $1, $2, $5, $10, $20, $50, and $100.

Insert your code into canonical_coin_systems.py.

Here are examples of interactions: 

$ python3 canonical_coin_systems.py
Input the desired amount: 10

1 banknote is needed.
The detail is:
$10: 1

$ python3 canonical_coin_systems.py
Input the desired amount: 739

12 banknotes are needed
The detail is:
$100: 7
 $20: 1
 $10: 1
  $5: 1
  $2: 2

$ python3 canonical_coin_systems.py
Input the desired amount: 35642

359 banknotes are needed
The detail is:
$100: 356
 $20: 2
  $2: 1