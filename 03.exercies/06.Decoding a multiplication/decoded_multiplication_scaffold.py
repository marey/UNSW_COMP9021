# Decodes all multiplications of the form
#
#                        *  *  *
#                   x       *  *
#                     ----------
#                     *  *  *  *
#                     *  *  *
#                     ----------
#                     *  *  *  *
#
# such that the sum of all digits in all 4 columns is constant.


for x in range(100, 1_000):
    for y in range(10, 100):
        pass
        # Replace pass above with your code.
        # Compute the first partial product product0, namely, x * (y % 10),
        # and make sure it is at least equal to 1000.
        # Compute the second partial product product1 and make sure it is smaller than 1000.
        # Perform all other necessary tests...
