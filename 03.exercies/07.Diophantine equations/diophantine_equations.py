# Written by Eric Martin for COMP9021


def diophantine(equation):
    a_x_plus_b, c = equation.replace(' ', '').split('y=')
    c = int(c)
    a, b = a_x_plus_b.split('x')
    a = int(a)
    b = int(b)
    equation = f'{a}x + {b}y = {c}' if b >= 0 else f'{a}x - {-b}y = {c}'
    # gcd = gcd(|a|,|b|)
    # x|a| + y|b| = gcd
    gcd, x, y = extended_euclid(abs(a), abs(b))
    if c % gcd:
        print(equation, 'has no solution.')
        return
    m = c // gcd
    a_sign = 2 * (a > 0) - 1
    b_sign = 2 * (b > 0) - 1
    x *= a_sign * m
    y *= b_sign * m
    # At this point, x.a + y.b = c.
    # Since lcm(a,b).gcd(a,b) = |a||b|, solutions are of the form
    # x.a + |b|/gcd.n + y.b - sign_product|a|/gcd.n = c, hence of the
    # form x.a + x_step.n + y.b - sign_product.y_step.n = c.
    x_step = abs(b) // gcd
    y_step = abs(a) // gcd
    sign_product = a_sign * b_sign
    # As x_step is positive, x % x_step is positive.
    # Changing x to x % x_step requires to:
    # - if x // x_step > 0, subtracting x_step from x,
    #   x // x_step times;
    # - if x // x_step < 0, adding x_step to x, -(x // x_step) times.
    # It is then necessary to:
    # - if x // x_step > 0, addding sign_product.y_step to y,
    #   x // x_step times;
    # - if x // x_step < 0, subtracting sign_product.y_step from x,
    #   -(x // x_step) times.
    y += x // x_step * sign_product * y_step
    x %= x_step
    if x_step == 1:
        x_step = '' 
    if y_step == 1:
        y_step = ''
    print(equation, 'has as solutions all pairs of the form')
    if not x:
        if x_step == '':
            print('    (n,', end=' ')
        else:
            print(f'    ({x} + {x_step}n,', end=' ')
    else: 
        print(f'    ({x} + {x_step}n,', end=' ')
    if not y:
        if y_step == '':
            print(f'{sign_product == 1 and "-n" or "n"})', end=' ')
        else:
            print(f'{-sign_product * y_step}n)', end=' ')
    elif sign_product < 0:
        print(f'{y} + {y_step}n)', end=' ')
    else:
        print(f'{y} - {y_step}n)', end=' ')
    print('with n an arbitrary integer.')
    
def extended_euclid(a, b):
    if b == 0:
        return a, 1, 0
    gcd, x, y = extended_euclid(b, a % b)
    return gcd, y, x - (a // b) * y
