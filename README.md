# sudoku-solver
This should be simple console Sudoku solver. In development now.

## Implemented features:
+ Field pretty printing.
+ Checking for correctness.
+ Solving simple (when there is only 1 unknown cell in column, row or square) cells.

## TODO:
+ Solving unobvious situations using tree-solution.
+ Examples

## Dependencies:
1. [python3.5](https://www.python.org/downloads/release/python-350/) required

## Usage:
You should create your field 9x9 size with zeros instead of unknown elements.
Then import sudoku class, create instance and set your field like this:

```
import Sudoku
sudoku = Sudoku()
field = [[....]]  # create your field here
sudoku.fill_field(field)
```

Solve your sudoku like this:

```
from solver import solve
solve(sudoku)
```
