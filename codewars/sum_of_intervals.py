"""
Write a function called sumIntervals/sum_intervals() that accepts an array of
intervals, and returns the sum of all the interval lengths. Overlapping
intervals should only be counted once.

Intervals

Intervals are represented by a pair of integers in the form of an array. The
first value of the interval will always be less than the second value.
Interval example: [1, 5] is an interval from 1 to 5.
The length of this interval is 4.

Overlapping Intervals

List containing overlapping intervals:

[
   [1,4],
   [7, 10],
   [3, 5]
]
The sum of the lengths of these intervals is 7. Since [1, 4] and [3, 5]
overlap, we can treat the interval as [1, 5], which has a length of 4.
"""


def sum_of_intervals(intervals):
    intervals.sort(key=lambda x: x[0])
    res_intervals = [list(intervals[0])]
    for interval in intervals[1:]:
        last_res_interval = res_intervals[-1]
        if interval[0] <= last_res_interval[1] < interval[1]:
            last_res_interval[1] = interval[1]
        if interval[0] > last_res_interval[1]:
            res_intervals.append(list(interval))
    return sum(x[1] - x[0] for x in res_intervals)


# best practice
def sum_of_intervals2(intervals):
    result = set()
    for start, stop in intervals:
        for x in range(start, stop):
            result.add(x)

    return len(result)


def tests():
    assert sum_of_intervals([(1, 4), (7, 10), (3, 5)]) == 7
