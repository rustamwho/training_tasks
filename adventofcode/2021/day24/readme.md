# --- Day 24: Arithmetic Logic Unit ---

### Click [me](https://adventofcode.com/2021/day/24) to open the task.

**Input puzzle** - ALU commands.

We can decode input instruction.
The monad repeat the same pattern for 14 times, the pattern include 18 alu commands.

For example, first 18 commands for first digit in model number decode like this:
```
inp w			w = input()
mul x 0 		x = 0
add x z			x += z
mod x 26		x %= 26
div z 1 		z //= 1
add x 12 		x += 12
eql x w 		x = 1 if x == w else 0      
eql x 0 		x = 1 if x == 0 else 0  
mul y 0 		y = 0                                       w = input()
add y 25        ==>     y = 25                      ==>             z *= 26     
mul y x 		y *= x                                      z += w + 7
add y 1 		y += 1
mul z y 		z *= y
mul y 0 		y = 0
add y w 		y += w
add y 7 		y += 7
mul y x 		y *= x
add z y 		z += y
```

After decode we can notice that everything depends on 3 commands/data - add x, div z, add y.