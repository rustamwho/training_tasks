import sys

j = sys.stdin.readline().strip()
s = sys.stdin.readline().strip()

result = sum(1 for symbol in s if symbol in j)

print(result)