# fchess - Minimax Chess Engine

This project is a very basic implementation of a chess engine that uses
Minimax with Alpha-Beta Pruning to analyze positions and choose a move to 
play.

Also, it comes with two heuristic options out of the box:
- Point Value (pvals): uses only pieces base-values as an evaluation method
- Piece-Square Table (bvals): uses base-values **and** board position

## Dependencies:

The only dependency is `python-chess`.

## Usage:

```
Usage: python3 fchess.py board ui white wdiff black bdiff
board: board file in Forsyth-Edwards Notation (FEN)
ui:    which UI will be used? [term / nint]
white: who will play as white? [human, ai00, ..., ai03]
wdiff: white AI difficulty (irrelevant for human and ai00)
black: who will play as black? [human, ai00, ..., ai03]
bdiff: black AI difficulty (irrelevant for human and ai00)

Example 1: python3 fchess.py boards/default term human 0 ai02 3
Example 2: python3 fchess.py boards/default nint ai01 3 ai02 3 >> output.txt
```

## License

fchess 1.0

Copyright (C) 2020 Felipe V. Calderan <fvcalderan@gmail.com>
 
This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.
 
You should have received a copy of the GNU General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.

