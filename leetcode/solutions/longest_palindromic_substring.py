def longest_palindrome(s: str) -> str:
    if s == '':
        return s
    start, end = 0, 0

    for i in range(len(s)):
        len1 = expand_from_center(s, i, i)
        len2 = expand_from_center(s, i, i + 1)
        max_len = max(len1, len2)
        if max_len > end - start:
            start = i - (max_len - 1) // 2
            end = i + max_len // 2

    return s[start:end + 1]


def expand_from_center(s, idx1, idx2):
    while idx1 >= 0 and idx2 < len(s) and s[idx1] == s[idx2]:
        idx1 -= 1
        idx2 += 1
    return idx2 - idx1 - 1


print(longest_palindrome('baabd'))
