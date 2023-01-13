Let a strictly positive integer n be given. Let D be the set of divisors of n. Let k be the number of prime divisors of n (that is, the number of prime numbers in D). The members of D can be arranged as the vertices of a solid in a k-dimensional space as illustrated below for n = 12 (in which case D = {1,2,3,4,6,12} and k = 2) and for n = 30 (in which case D = {1,2,3,5,6,10,15,30} and k = 3).

Each of the solids' vertices is associated with two collections of nodes: those "directly below'' it, and those "directly above'' it. In particular, the prime divisors of n are "directly above'' 1, and no vertex is below 1; n has exactly k vertices "directly below'' it, and no vertex is above n. This suggests considering a dictionary whose keys are the members of D (inserted from smallest to largest), and as value for a given key d, the pair of ordered lists of members of D "directly below'' d and "directly above'' d, respectively.

The solids exhibit k distinct "edge directions'', one for each prime divisor of n, defining a partition of the solids' edges. One can represent this partition as a dictionary whose keys are the prime divisors of n (inserted from smallest to largest), and as value for a given key p, the ordered list of ordered pairs of members of D that make up the endpoints of the edges whose "direction'' is associated with p.


The program hasse_diagram.py defines a function make_hasse_diagram() that returns a named tuple HasseDiagram with three attributes:

factors, for a dictionary whose keys are the members of D, and as value for a given key d (1 excepted), a string that represents the prime decomposition of d, using x for multiplication and ^ for exponentiation, displaying only exponents greater than 1;

vertices, for the first dictionary previously defined;

edges, for the second dictionary previously defined.

Replace pass in hasse_diagram.py with your code.

Except for namedtuple, hasse_diagram.py imports a number of classes and functions from various modules that are used in the solution, but that other good solutions will make no use of.