## Encoding pairs of integers as natural numbers

Complete the program plane_encoding.py that implements a function encode(a, b) and a function decode(n) for the one-to-one mapping from the set of pairs of integers onto the set of natural numbers, that can be graphically described as follows:


That is, starting from the point (0, 0) of the plane, we move to (1, 0) and then spiral counterclockwise:

encode(0,0) returns 0 and decode(0) returns (0,0)

encode(1,0) returns 1 and decode(1) returns (1,0)

encode(1,1) returns 2 and decode(2) returns (1,1)

encode(0,1) returns 3 and decode(3) returns (0,1)

encode(-1,1) returns 4 and decode(4) returns (-1,1)

encode(-1,0) returns 5 and decode(5) returns (-1,0)

encode(-1,-1) returns 6 and decode(6) returns (-1,-1)

encode(0,-1) returns 7 and decode(7) returns (0,-1)

encode(1,-1) returns 8 and decode(8) returns (1,-1)

encode(2,-1) returns 9 and decode(9) returns (2,-1)
 . . . 