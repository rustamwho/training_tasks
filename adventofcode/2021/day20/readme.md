# --- Day 20: Trench Map ---

### Click [me](https://adventofcode.com/2021/day/20) to open the task.

**Input puzzle** - image enhancement algorithm and input image.

#### Part 1
Applying the image enhancement algorithm to image twice.

The vital line:
```python
default = 0 if algorithm[0] == 0 or i % 2 == 0 else 1
```
Because pixels outside the borders of the image give an index of 0.
However, in the algorithm, '#' (1) comes first.

#### Part 2
Applying the image enhancement algorithm to image 50 times.