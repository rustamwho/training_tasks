# --- Day 17: Trick Shot ---

### Click [me](https://adventofcode.com/2021/day/17) to open the task.

**Input puzzle** - target area coordinates.

#### Part 1
We need to calculate highest y position.
1) Find the best trajectory. It is when y=0 velocity of y (Vy)=-<target_area_y_min>-1.
```
   For example, min target area y=-10. 
   After we go up we'll back down at y=0 with a Vy = -n-1. So -target_min_y - 1 is the maximum value that after reach y=0 get in the range.
   With y = 9 we'll reach y = 0 with y velocity = -10. The next step we'll be at y=-10 that is in the range.
   Instead if we choose y = 10 we'll reach y=0 with y velocity = -11. The next stel we'll be at y=-11 that is out of range.
```
2) Thanks to the infinite series formula, we can calculate the maximum height for this trajectory.
```
    Vy * (Vy+1) / 2
```

#### Part 2
Calculate count distinct initial velocity values cause the probe to be within the target area after any step.

1) Find count of steps from y=0 to target area for every relevant Vy.
2) Find count of steps from x=0 to target area for every relevant Vx.
3) Calculate count of (Vx,Vy) where steps count are same.