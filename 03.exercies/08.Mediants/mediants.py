# Written by Eric Martin for COMP9021


from math import gcd


def bottom_up_mediants_to(p, q):
    if p == 0:
        print('0/1')
        return
    p, q = normalise(p, q)
    if q == 1:
        print(f'{p}/1')
        return
    left = p // q, 1
    right = left[0] + 1, 1
    target = p, q
    mediant = left[0] + right[0], 2
    dichotomies = []
    w =  max(len(str(p)), len(str(q)))
    while mediant != target:
        on_right_side = mediant[0] * target[1] < target[0] * mediant[1]
        print_nonfinal_dichotomy(left, mediant, right, on_right_side, w)
        if on_right_side:
            left = mediant
        else:            
            right = mediant                           
        mediant = left[0] + right[0], left[1] + right[1]
    print_dichotomy(left, ' ', mediant, ' ', right, w)

def normalise(p, q):
    the_gcd = gcd(p, q)
    p //= the_gcd
    q //= the_gcd
    if q < 0:
        p = -p
        q = -q
    return p, q

def print_nonfinal_dichotomy(left, mediant, right, on_right_side, w):
    marks = {True: '*', False: ' '}
    print_dichotomy(left, marks[not on_right_side], mediant,
                    marks[on_right_side], right, w
                   )

def print_dichotomy(left, left_mark, mediant, right_mark, right, w):
    marks = {True: '*', False: ' '}
    print(f'{left[0]:{w}}/{left[1]:<{w}}  {left_mark}  '
          f'{mediant[0]:{w}}/{mediant[1]:<{w}}  {right_mark}  '
          f'{right[0]:{w}}/{right[1]:<{w}}'
         )
    
def top_down_mediants_from(p, q):
    return [f'{x}/{y}' if y != 1 else str(x)
                for (x, y) in sorted(mediants_from(p, q),
                                     key=lambda f: f[0] / f[1]
                                    )
           ]

def mediants_from(p, q):
    if p == 0:
        return [(0, 1)]
    p, q = normalise(p, q)
    fractions_to_process = [(p, q)]
    mediants = set()
    while fractions_to_process:
        p, q = fractions_to_process.pop()
        mediants.add((p, q))
        if q == 1:
            continue
        x, y = extended_euclid(p, -q)
        n = -x // q + 1
        p_prime = y + p * n
        q_prime = x + q * n
        fractions_to_process.extend(((p_prime, q_prime),
                                     (p - p_prime, q - q_prime)
                                    )
                                   )
    return mediants

def extended_euclid(p, q):
    if q == 0:
        return 1, 0
    x, y = extended_euclid(q, p % q)
    return y, x - (p // q) * y
