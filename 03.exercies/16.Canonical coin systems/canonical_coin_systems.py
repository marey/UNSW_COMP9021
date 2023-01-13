# Written by Eric Martin for COMP9021


try:
    amount = int(input('Input the amount: '))
    if amount < 0:
        raise ValueError
except ValueError:
    print('Incorrect value, try again.')
face_values = [1, 2, 5, 10, 20, 50, 100]
coins = {}
amount_left = amount
while amount_left:
    value = face_values.pop()
    if amount_left >= value:
        coins[value] = amount_left // value
        amount_left %= value
nb_of_coins = sum(coins.values())
if nb_of_coins == 0:
    print('\nNo coin is needed.')
elif nb_of_coins == 1:
    print(f'\nOne coin of value ${amount} is needed.')
else:
    print(f'\n{nb_of_coins} coins are needed. The detail is:')
    for value in coins:
        print(f'{"$" + str(value):>8}: {coins[value]}')
