def length_of_longest_substring(s: str) -> int:
    start = length = 0
    hashmap = {}  # For saving used symbols and their last indices

    for end, value in enumerate(s):
        if value in hashmap:
            start = max(start, hashmap[value] + 1)
        hashmap[value] = end
        length = max(length, end - start + 1)
        print(f'symbol={s[end]}, start={start}, end={end}, length={length}, '
              f'hashmap={hashmap}')

    return length


print(length_of_longest_substring('abcabcdebb'))
