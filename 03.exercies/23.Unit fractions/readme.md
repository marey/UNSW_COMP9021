Unit fractions
Let NN and DD be two strictly positive integers with N<DN<D. The fraction N/DN/D can be written as a sum of unit fractions, that is, there exists integers k,d_1,\ldots,d_k\geq 1k,d 
1
​
 ,…,d 
k
​
 ≥1 with d_1<d_2<\ldots<d_kd 
1
​
 <d 
2
​
 <…<d 
k
​
  such that

\frac{N}{D} = \frac{1}{d_1}+\frac{1}{d_2}+\dots+\frac{1}{d_k} 
D
N
​
 = 
d 
1
​
 
1
​
 + 
d 
2
​
 
1
​
 +⋯+ 
d 
k
​
 
1
​
 .

There are actually infinitely many such representations. Indeed, since

1=\frac{1}{2}+\frac{1}{3}+\frac{1}{6}1= 
2
1
​
 + 
3
1
​
 + 
6
1
​
 

if \frac{N}{D} = \frac{1}{d_1}+\frac{1}{d_2}+\dots+\frac{1}{d_k} 
D
N
​
 = 
d 
1
​
 
1
​
 + 
d 
2
​
 
1
​
 +⋯+ 
d 
k
​
 
1
​
  then also

\frac{N}{D} = \frac{1}{d_1}+\frac{1}{d_2}+\dots+\frac{1}{d_{k-1}}+\frac{1}{2d_k}+\frac{1}{3d_k}+\frac{1}{6d_k} 
D
N
​
 = 
d 
1
​
 
1
​
 + 
d 
2
​
 
1
​
 +⋯+ 
d 
k−1
​
 
1
​
 + 
2d 
k
​
 
1
​
 + 
3d 
k
​
 
1
​
 + 
6d 
k
​
 
1
​
 .


One particular representation is obtained by a method proposed by Fibonacci, in the form of a greedy algorithm. Suppose that N/DN/D cannot be simplified, that is, NN and DD have no other common factor but 1. If N=1N=1 then we are done, so suppose otherwise. Let d_1d 
1
​
  be the smallest integer such that \frac{N}{D} 
D
N
​
  can be written as \frac{1}{d_1}+f_1 
d 
1
​
 
1
​
 +f 
1
​
 , with f_1f 
1
​
  necessarily strictly positive by assumption. Looking for the smallest d_1d 
1
​
  is what makes the algorithm greedy. Of course, d_1d 
1
​
  is equal to D\div N + 1D÷N+1. By the choice of d_1d 
1
​
 , \frac{1}{d_1-1}>\frac{N}{D} 
d 
1
​
 −1
1
​
 > 
D
N
​
 , hence D>N(d_1-1)D>N(d 
1
​
 −1), hence N>Nd_1-DN>Nd 
1
​
 −D. Since f_1f 
1
​
  is equal to \frac{N}{D}-\frac{1}{d_1}=\frac{Nd_1-D}{Dd_1} 
D
N
​
 − 
d 
1
​
 
1
​
 = 
Dd 
1
​
 
Nd 
1
​
 −D
​
 , it follows that \frac{N}{D} 
D
N
​
  can be written as \frac{1}{d_1}+\frac{N_1}{D_1} 
d 
1
​
 
1
​
 + 
D 
1
​
 
N 
1
​
 
​
  with N_1<NN 
1
​
 <N. If N_1>1N 
1
​
 >1 then the same argument allows one to greedily find d_2>d_1d 
2
​
 >d 
1
​
  such that for some strictly positive integers N_2N 
2
​
  and D_2D 
2
​
 , \frac{N}{D} 
D
N
​
  can be written as \frac{1}{d_1}+\frac{1}{d_2}+\frac{N_2}{D_2} 
d 
1
​
 
1
​
 + 
d 
2
​
 
1
​
 + 
D 
2
​
 
N 
2
​
 
​
  with N_2<N_1N 
2
​
 <N 
1
​
 , and if N_2>1N 
2
​
 >1 then the same argument allows one to greedily find d_3>d_2d 
3
​
 >d 
2
​
  such that for some strictly positive integers N_3N 
3
​
  and D_3D 
3
​
 , \frac{N}{D} 
D
N
​
  can be written as \frac{1}{d_1}+\frac{1}{d_2}+\frac{1}{d_3}+\frac{N_3}{D_3} 
d 
1
​
 
1
​
 + 
d 
2
​
 
1
​
 + 
d 
3
​
 
1
​
 + 
D 
3
​
 
N 
3
​
 
​
  with N_3<N_2N 
3
​
 <N 
2
​
 ... After a finite number of steps, we are done.

The number of summands in the sum of unit fractions given by Fibonacci's method is not always minimal: it is sometimes possible to decompose \frac{N}{D} 
D
N
​
  as sum of unit fractions with fewer summands. For instance, Fibonacci's method yields

\frac{4}{17} = \frac{1}{5} + \frac{1}{29} + \frac{1}{1233} + \frac{1}{3039345} 
17
4
​
 = 
5
1
​
 + 
29
1
​
 + 
1233
1
​
 + 
3039345
1
​
 

whereas \frac{4}{17} 
17
4
​
  can be written as a sum of 3 unit fractions, actually in 4 possible ways:

\frac{4}{17} = \frac{1}{5} + \frac{1}{30} + \frac{1}{510} 
17
4
​
 = 
5
1
​
 + 
30
1
​
 + 
510
1
​
 

\frac{4}{17} = \frac{1}{5} + \frac{1}{34} + \frac{1}{170} 
17
4
​
 = 
5
1
​
 + 
34
1
​
 + 
170
1
​
 

\frac{4}{17} = \frac{1}{6} + \frac{1}{15} + \frac{1}{510} 
17
4
​
 = 
6
1
​
 + 
15
1
​
 + 
510
1
​
 

\frac{4}{17} = \frac{1}{6} + \frac{1}{17} + \frac{1}{102} 
17
4
​
 = 
6
1
​
 + 
17
1
​
 + 
102
1
​
 


Complete the program unit_fractions.py so as to have the functionality of the two functions:

fibonacci_decomposition(N, D), that takes two strictly positive integers NN and DD as arguments, and writes N/DN/D as a sum of unit fractions following Fibonacci method, plus an integer in case N ≥ DN≥D (in a unique way)

shortest_length_decompositions(), that also takes two strictly positive integers NN and DD as arguments, and writes N/DN/D as a sum of unit fractions with a minimal number of summands, plus an integer in case N ≥ D (in possibly many ways)


Here are possible interactions:

 >>> from unit_fractions import *
 >>> fibonacci_decomposition(1, 521)
 1/521 = 1/521
 >>> fibonacci_decomposition(521, 521)
 521/521 = 1
 >>> fibonacci_decomposition(521, 1050)
 521/1050 = 1/3 + 1/7 + 1/50
 >>> fibonacci_decomposition(1050, 521)
 1050/521 = 2 + 1/66 + 1/4913 + 1/33787684 + 1/2854018941421956
 >>> fibonacci_decomposition(6, 7)
 6/7 = 1/2 + 1/3 + 1/42
 >>> shortest_length_decompositions(6, 7)
 6/7 = 1/2 + 1/3 + 1/42
 >>> fibonacci_decomposition(8, 11)
 8/11 = 1/2 + 1/5 + 1/37 + 1/4070
 >>> shortest_length_decompositions(8, 11)
 8/11 = 1/2 + 1/5 + 1/37 + 1/4070
 8/11 = 1/2 + 1/5 + 1/38 + 1/1045
 8/11 = 1/2 + 1/5 + 1/40 + 1/440
 8/11 = 1/2 + 1/5 + 1/44 + 1/220
 8/11 = 1/2 + 1/5 + 1/45 + 1/198
 8/11 = 1/2 + 1/5 + 1/55 + 1/110
 8/11 = 1/2 + 1/5 + 1/70 + 1/77
 8/11 = 1/2 + 1/6 + 1/17 + 1/561
 8/11 = 1/2 + 1/6 + 1/18 + 1/198
 8/11 = 1/2 + 1/6 + 1/21 + 1/77
 8/11 = 1/2 + 1/6 + 1/22 + 1/66
 8/11 = 1/2 + 1/7 + 1/12 + 1/924
 8/11 = 1/2 + 1/7 + 1/14 + 1/77
 8/11 = 1/2 + 1/8 + 1/10 + 1/440
 8/11 = 1/2 + 1/8 + 1/11 + 1/88
 8/11 = 1/3 + 1/4 + 1/7 + 1/924
 >>> fibonacci_decomposition(4, 17)
 4/17 = 1/5 + 1/29 + 1/1233 + 1/3039345
 >>> shortest_length_decompositions(4, 17)
 4/17 = 1/5 + 1/30 + 1/510
 4/17 = 1/5 + 1/34 + 1/170
 4/17 = 1/6 + 1/15 + 1/510
 4/17 = 1/6 + 1/17 + 1/102 