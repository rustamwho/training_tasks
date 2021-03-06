# --- Day 23: Amphipod ---

### Click [me](https://adventofcode.com/2021/day/23) to open the task.

**Input puzzle** - diagram of the situation, including locations of each amphipod (A, B, C, or D, each of which is occupying an otherwise open space), walls (#), and open space (.).

#### Part 1
Every movement of the amphipods expends energy. We need to find a way with minimal energy consumption. A - 1, B - 10, C - 100, D - 1000.


I didn't start programming, it was interesting to solve manually.
```
#############
#...........#
###D#B#C#A###
  #C#A#D#B#
  #########

Step 1: 2
#############
#.........A.#
###D#B#C#.###
  #C#A#D#B#
  #########

Step 2: 20
#############
#.....B...A.#
###D#.#C#.###
  #C#A#D#B#
  #########
  
Step 3: 5
#############
#.A...B...A.#
###D#.#C#.###
  #C#.#D#B#
  #########

Step 4: 30
#############
#.A.......A.#
###D#.#C#.###
  #C#B#D#B#
  #########

Step 5: 70
#############
#.A.......A.#
###D#B#C#.###
  #C#B#D#.#
  #########

Step 6: 200
#############
#.A...C...A.#
###D#B#.#.###
  #C#B#D#.#
  #########

Step 7: 6000
#############
#.A...C...A.#
###D#B#.#.###
  #C#B#.#D#
  #########

Step 8: 300
#############
#.A.......A.#
###D#B#.#.###
  #C#B#C#D#
  #########

Step 9: 8000
#############
#.A.......A.#
###.#B#.#D###
  #C#B#C#D#
  #########

Step 10: 700
#############
#.A.......A.#
###.#B#C#D###
  #.#B#C#D#
  #########

Step 11: 3
#############
#.........A.#
###.#B#C#D###
  #A#B#C#D#
  #########

Step 12: 8
#############
#.........A.#
###.#B#C#D###
  #A#B#C#D#
  #########

2 + 20 + 5 + 30 + 70 + 200 + 6000 + 300 + 8000 + 700 + 3 + 8 = 15 338

```


#### Part 2
Larger input puzzle.
``` 
#############
#...........#
###D#B#C#A###
  #D#C#B#A#
  #D#B#A#C#
  #C#A#D#B#
  #########

Step 1: 9
#############
#A..........#
###D#B#C#.###
  #D#C#B#A#
  #D#B#A#C#
  #C#A#D#B#
  #########

Step 2: 9
#############
#AA.........#
###D#B#C#.###
  #D#C#B#.#
  #D#B#A#C#
  #C#A#D#B#
  #########

Step 3: 500
#############
#AA........C#
###D#B#C#.###
  #D#C#B#.#
  #D#B#A#.#
  #C#A#D#B#
  #########

Step 4: 50
#############
#AA.......BC#
###D#B#C#.###
  #D#C#B#.#
  #D#B#A#.#
  #C#A#D#.#
  #########

Step 5: 11000
#############
#AA.......BC#
###.#B#C#.###
  #D#C#B#.#
  #D#B#A#.#
  #C#A#D#D#
  #########

Step 6: 11000
#############
#AA.......BC#
###.#B#C#.###
  #.#C#B#.#
  #D#B#A#D#
  #C#A#D#D#
  #########

Step 7: 11000
#############
#AA.......BC#
###.#B#C#.###
  #.#C#B#D#
  #.#B#A#D#
  #C#A#D#D#
  #########

Step 8: 900
#############
#AA.....C.BC#
###.#B#C#.###
  #.#C#B#D#
  #.#B#A#D#
  #.#A#D#D#
  #########

Step 9: 5
#############
#A......C.BC#
###.#B#C#.###
  #.#C#B#D#
  #.#B#A#D#
  #A#A#D#D#
  #########

Step 10: 5
#############
#.......C.BC#
###.#B#C#.###
  #.#C#B#D#
  #A#B#A#D#
  #A#A#D#D#
  #########

Step 11: 20
#############
#.....B.C.BC#
###.#.#C#.###
  #.#C#B#D#
  #A#B#A#D#
  #A#A#D#D#
  #########
 
Step 12: 600
#############
#C....B.C.BC#
###.#.#C#.###
  #.#.#B#D#
  #A#B#A#D#
  #A#A#D#D#
  #########

Step 13: 60
#############
#CB...B.C.BC#
###.#.#C#.###
  #.#.#B#D#
  #A#.#A#D#
  #A#A#D#D#
  #########

Step 14: 8
#############
#CB...B.C.BC#
###.#.#C#.###
  #A#.#B#D#
  #A#.#A#D#
  #A#.#D#D#
  #########

Step 15: 50
#############
#CB.....C.BC#
###.#.#C#.###
  #A#.#B#D#
  #A#.#A#D#
  #A#B#D#D#
  #########

Step 16: 60
#############
#C......C.BC#
###.#.#C#.###
  #A#.#B#D#
  #A#B#A#D#
  #A#B#D#D#
  #########

Step 17: 600
#############
#CC.....C.BC#
###.#.#.#.###
  #A#.#B#D#
  #A#B#A#D#
  #A#B#D#D#
  #########

Step 18: 60
#############
#CC.....C.BC#
###.#.#.#.###
  #A#B#.#D#
  #A#B#A#D#
  #A#B#D#D#
  #########

Step 19: 8
#############
#CC.....C.BC#
###A#.#.#.###
  #A#B#.#D#
  #A#B#.#D#
  #A#B#D#D#
  #########
  
Step 20: 5000
#############
#CC...D.C.BC#
###A#.#.#.###
  #A#B#.#D#
  #A#B#.#D#
  #A#B#.#D#
  #########

Step 21: 500
#############
#CC...D...BC#
###A#.#.#.###
  #A#B#.#D#
  #A#B#.#D#
  #A#B#C#D#
  #########

Step 22: 4000
#############
#CC.......BC#
###A#.#.#D###
  #A#B#.#D#
  #A#B#.#D#
  #A#B#C#D#
  #########

Step 23: 60
#############
#CC........C#
###A#B#.#D###
  #A#B#.#D#
  #A#B#.#D#
  #A#B#C#D#
  #########

Step 24: 800
#############
#C.........C#
###A#B#.#D###
  #A#B#.#D#
  #A#B#C#D#
  #A#B#C#D#
  #########

Step 25: 600
#############
#C..........#
###A#B#.#D###
  #A#B#C#D#
  #A#B#C#D#
  #A#B#C#D#
  #########

Step 26: 700
#############
#...........#
###A#B#C#D###
  #A#B#C#D#
  #A#B#C#D#
  #A#B#C#D#
  #########


9+9+500+50+11000+11000+11000+900+5+5+20+600+60+8+50+60+600+60+8+5000+500+4000+60+800+600+700 = 47 604
```