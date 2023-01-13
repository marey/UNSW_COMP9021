The 8 puzzle
Dispatch the integers from 0 to 8, with 0 possibly changed to None, as a list of 3 lists of size 3, to represent a 9 puzzle.

For instance, let  [[4, 0, 8], [1, 3, 7], [5, 2, 6]] or [[4, None ,8], [1, 3, 7], [5, 2, 6]] represent the 9 puzzle


with the 8 integers being printed on 8 tiles that are placed in a frame with one location being tile free.

The aim is to slide tiles horizontally or vertically so as to eventually reach the configuration


It can be shown that the puzzle is solvable iff the permutation of the integers 1, ..., 8, determined by reading those integers off the puzzle from top to bottom and from left to right, is even. This is clearly a necessary condition since:

sliding a tile horizontally does not change the number of inversions;

sliding a tile vertically changes the number of inversions by -2, 0 or 2;

the parity of the identity is even. 

Complete the program eight_puzzle.py so as to have the functionality of the two functions:

validate_8_puzzle(grid) that prints out whether or not grid is a valid representation of a solvable 8 puzzle;

solve_8_puzzle(grid) that, assuming that grid is a valid representation of a solvable 8 puzzle, outputs a solution to the puzzle characterised as follows:

the number of moves is minimal;

at every stage, the preferences of the tile to slide are, from most preferred to least preferred:

the tile above the empty cell (provided the latter is not in the top row), then

the tile to the left of the empty cell (provided the latter is not in the left column), then

the tile to the right of the empty cell (provided the latter is not in the right column), then

the tile below the empty cell (provided the latter is not in the bottom row).

Also see the corresponding Jupyter notebook sheet for a description of a possible algorithmic approach to implement solve_8_puzzle(grid).