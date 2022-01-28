# --- Day 19: Beacon Scanner ---

### Click [me](https://adventofcode.com/2021/day/19) to open the task.

**Input puzzle** - positions of beacons from scanners (coordinates x,y,z).

#### Part 1

We need to calculate the number of beacons.

For this:

1) The scanner 0 is taken for the correct direction.
2) Search for matching positions of beacons at 24 different orientations of
   each scanner.
3) Thus, we find the correct positions of scanners and beacons relative to
   scanner 0.

#### Part 2

We need to find the
largest [Manhattan distance](https://en.wikipedia.org/wiki/Taxicab_geometry)
between any two scanner.

1) In the part 1 we already found the correct positions of the scanners (relative to scanner 0).
2) Calculate Manhattan distance between any two scanners and return max value:

```python
x1, y1, z1 = coordinate_of_the_first_scanner
x2, y2, z2 = coordinate_of_the_second_scanner

manhattan_distance = abs(x2 - x1) + abs(y2 - y1) + abs(z2 - z1)
```
