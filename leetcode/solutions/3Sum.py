def three_sum(nums: list[int]) -> list[list[int]]:
    """Easy way."""
    hashmap = {}
    result = []
    nums.sort()

    for i, x in enumerate(nums):
        target = 0 - x
        for j, y in enumerate(nums[i + 1:]):
            hashmap[y] = j
        for j, y in enumerate(nums[i + 1:]):
            complement = target - y
            if complement < y:
                break
            if complement in hashmap and hashmap[complement] > j:
                new = [x, y, complement]
                if new not in result:
                    result.append(new)

    return result


def find_triplets(nums):
    """Faster and uses less memory usage."""
    n = len(nums)
    # Sort the input array
    nums.sort()
    triplets = []

    # For handling the cases when no such triplets exits.
    flag = False

    # Iterate over the array from start to n-2.
    for i in range(n - 2):
        if i == 0 or nums[i] > nums[i - 1]:

            # Index of the first element in remaining range
            start = i + 1
            # Index of the last element
            end = n - 1
            # Setting our new target
            target = 0 - nums[i]

            while start < end:

                # Checking if current element is same as previous
                if start > i + 1 and nums[start] == nums[start - 1]:
                    start += 1
                    continue

                # Checking if current element is same as previous
                if end < n - 1 and nums[end] == nums[end + 1]:
                    end -= 1
                    continue

                # If we found the triplets then print it and set the flag
                if target == nums[start] + nums[end]:
                    triplets.append([nums[i], nums[start], nums[end]])
                    flag = True
                    start += 1
                    end -= 1

                # If target is greater then increment the start index
                elif target > nums[start] + nums[end]:
                    start += 1

                # If target is smaller than decrement the end index
                else:
                    end -= 1
    return triplets


if __name__ == '__main__':
    print(three_sum([-1, 0, 1, 2, -1, -4]))

    filename = __file__.replace('solutions', 'inputs').replace('.py', '.txt')
    with open(filename) as f:
        input_nums = [int(x) for x in f.read()[1:-1].split(',')]
    print(find_triplets(input_nums))
