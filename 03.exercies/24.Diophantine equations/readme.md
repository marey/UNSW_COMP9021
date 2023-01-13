Diophantine equations
We consider Diophantine equations of the form ax+by=cax+by=c with aa and bb both not equal to 0. We will represent such an equation as a string of the form ax+by=c or ax-by=c where a and c are nonzero integer literals (not preceded by + in case they are positive) and where b is a strictly positive integer literal (not preceded by +), possibly with spaces anywhere at the beginning, at the end, and around the +, - and = characters. The equation ax+by=cax+by=c has a solution iff cc is a multiple of \gcd(a,b)gcd(a,b). In case cc is indeed a multiple of \gcd(a,b)gcd(a,b), then ax+by=cax+by=c has has infinitely many solutions, namely, all pairs (x,y)(x,y) of the form


\left(x_0 + \frac{\mathrm{lcm}(a,b)}{a}n,y_0 - \frac{\mathrm{lcm}(a,b)}{b}n\right)(x 
0
​
 + 
a
lcm(a,b)
​
 n,y 
0
​
 − 
b
lcm(a,b)
​
 n)


for arbitrary integers nn, where \mathrm{lcm}(a,b)lcm(a,b) denotes the least common multiplier of aa and bb, and where (x_0,y_0)(x 
0
​
 ,y 
0
​
 ) is a solution to the equation. That particular solution can be derived from the extended Euclidian algorithm, that yields not only \gcd(a,b)gcd(a,b) but also a pair of Bézout coefficients, namely, two integers xx and yy with ax+by=\gcd(a,b)ax+by=gcd(a,b). To normalise the representation of the solutions, we rewrite the equation above as

\left(x_0 + \frac{\mathrm{lcm}(a,b)}{|a|}n,y_0 - \mathrm{sign}(a)\frac{\mathrm{lcm}(a,b)}{b}n\right)(x 
0
​
 + 
∣a∣
lcm(a,b)
​
 n,y 
0
​
 −sign(a) 
b
lcm(a,b)
​
 n)

where \mathrm{sign}(a)sign(a) is 1 if aa is positive and -1 if aa is negative, and we impose that the pair (x_0,y_0)(x 
0
​
 ,y 
0
​
 ) is such that x_0x 
0
​
  is nonnegative and minimal.

Write a Python program diophantine_equation.py that defines a function diophantine() that prints out whether the equation provided as argument has a solution, and in case it does, prints out the normalised representation of its solutions. The output reproduces the equation nicely formatted, that is, with a single space around the +, - and = characters. As for the representation of the solutions, it is also nicely formatted, omitting x_0x 
0
​
  or y_0y 
0
​
  when they are equal to 0, and omitting 1 as a factor of nn. Press the Run or Mark buttons for possible interactions:

>>> diophantine('1x + 1y = 0')
1x + 1y = 0 has as solutions all pairs of the form
    (n, -n) with n an arbitrary integer.
>>> diophantine('-1x + 1y = 0')
-1x + 1y = 0 has as solutions all pairs of the form
    (n, n) with n an arbitrary integer.
>>> diophantine('1x - 1y = 0')
1x - 1y = 0 has as solutions all pairs of the form
    (n, n) with n an arbitrary integer.
>>> diophantine('-1x - 1y = 0')
-1x - 1y = 0 has as solutions all pairs of the form
    (n, -n) with n an arbitrary integer.
>>> diophantine('1x + 1y = -1')
1x + 1y = -1 has as solutions all pairs of the form
    (n, -1 - n) with n an arbitrary integer.
>>> diophantine('-1x + 1y = 1')
-1x + 1y = 1 has as solutions all pairs of the form
    (n, 1 + n) with n an arbitrary integer.
>>> diophantine('4x + 6y = 9')
4x + 6y = 9 has no solution.
>>> diophantine('4x + 6y = 10')
4x + 6y = 10 has as solutions all pairs of the form
    (1 + 3n, 1 - 2n) with n an arbitrary integer.
>>> diophantine('71x+83y=2')
71x + 83y = 2 has as solutions all pairs of the form
    (69 + 83n, -59 - 71n) with n an arbitrary integer.
>>> diophantine(' 782 x + 253 y = 92')
782x + 253y = 92 has as solutions all pairs of the form
    (4 + 11n, -12 - 34n) with n an arbitrary integer.
>>> diophantine('-123x -456y = 78')
-123x - 456y = 78 has as solutions all pairs of the form
    (118 + 152n, -32 - 41n) with n an arbitrary integer.
>>> diophantine('-321x +654y = -87')
-321x + 654y = -87 has as solutions all pairs of the form
    (149 + 218n, 73 + 107n) with n an arbitrary integer.

See the corresponding Jupyter notebook sheet for the mathematical details.