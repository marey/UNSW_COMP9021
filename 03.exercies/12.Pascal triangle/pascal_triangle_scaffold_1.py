# Prompts the user for a number N and prints out the first N + 1 lines of Pascal triangle.



while True:
    try:
        N = int(input('Enter a nonnegative integer: '))
        if N < 0:
            raise ValueError
        break
    except ValueError:
        print('Incorrect input, try again')

pascal_triangle = [[1] * (n + 1) for n in range(N + 1)]
for n in range(2, N + 1):
    # Insert your code to compute Pascal triangle
width = len(str(pascal_triangle[N][N // 2]))
# Insert yoru code to display Pascal triangle
