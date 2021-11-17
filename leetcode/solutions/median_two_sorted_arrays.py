import statistics


def find_median_sorted_arrays(nums1: list[int], nums2: list[int]):
    return statistics.median(nums1 + nums2)


print(find_median_sorted_arrays([1, 3], [2]))
