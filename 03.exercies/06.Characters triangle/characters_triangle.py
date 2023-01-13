# Written by Eric Martin for COMP9021


while True:
    try:
        height = int(input('Enter a strictly positive integer: '))
        if height <= 0:
            raise ValueError
        break
    except ValueError:
        print('Incorrect input, try again.')
A_code = ord('A')
c = A_code
for i in range(height):
    # Displays spaces on the left
    print(' ' * (height - i - 1), end='')
    # Displays letters before middle column
    for _ in range(i):
        print(chr(c), end='')
        # Code of next letter
        c = (c - A_code + 1) % 26 + A_code
    # Displays middle column
    print(chr(c), end='')
    # Displays letters after middle column
    for _ in range(i):
        # Code of previous letter
        c = (c - A_code - 1) % 26 + A_code
        print(chr(c), end='')
    print()
    # Code of first letter to be input on next line
    c = ((2 + i) * (1 + i) // 2) % 26 + A_code
