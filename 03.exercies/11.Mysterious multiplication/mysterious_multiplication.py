# Written by Eric Martin for COMP9021


seen_solution = False
for x in range(100, 1_000):
    for y in range(10, 100):
        product_0 = x * (y % 10)
        if product_0 < 1_000:
            continue
        product_1 = x * (y // 10)
        if product_1 >= 1_000:
            continue
        total = product_0 + 10 * product_1
        if total >= 10_000:
            continue
        the_sum = x % 10 + y % 10 + product_0 % 10 + total % 10
        if x // 10 % 10 + y // 10 + product_0 // 10 % 10 + product_1 % 10\
           + total // 10 % 10 != the_sum:
            continue
        if x // 100 + product_0 // 100 % 10 + product_1 // 10 % 10\
           + total // 100 % 10 != the_sum:
            continue
        if product_0 // 1_000 + product_1 // 100 + total // 1_000 == the_sum:
            if seen_solution:
                print()
            seen_solution = True
            print(f'A solution with all columns adding up to {the_sum}:')
            print('      ', ' '.join(c for c in str(x)))
            print('    ', 'x  ', ' '.join(c for c in str(y)))
            print('     -------')
            print('    ', ' '.join(c for c in str(product_0)))
            print('    ', ' '.join(c for c in str(product_1)))
            print('     -------')
            print('    ', ' '.join(c for c in str(total)))
