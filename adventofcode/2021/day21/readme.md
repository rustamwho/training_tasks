# --- Day 21: Dirac Dice ---

### Click [me](https://adventofcode.com/2021/day/21) to open the task.

**Input puzzle** - start positions for each of players.

#### Part 1
We need to simulate the simple game with a 100-sided die.
For this, use generator (return next 3 values).

#### Part 2
Recursion method for calculate count of win universe for each player. 
Game stop, when either player's score reaches at least 21.
Use ```functools.lru_cache``` for speed up.