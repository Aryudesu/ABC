import sys

S = input()
data = S.split("|")
result = [len(l) for l in data][1:-1]
print(*result)
