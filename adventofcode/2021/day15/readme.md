# --- Day 15: Chiton ---

### Click [me](https://adventofcode.com/2021/day/15) to open the task.

**Input puzzle** - grid with risk level for every point.

We need to find the best path from the top left to bottom right and calculate lowest total risk for it.

#### Part 1
Use [Dijkstra's algorithm](https://en.wikipedia.org/wiki/Dijkstra%27s_algorithm) for finding the shortest paths between nodes in a graph. 
For storage unvisited neighbors nodes used Heap from heapq.

#### Part 2
We need to build full grid (25 times more than the original). And use Dijkstra's algorithm from part 1.