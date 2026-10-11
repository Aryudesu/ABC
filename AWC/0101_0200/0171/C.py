from sys import stdin

readline = stdin.readline
N, K = map(int, readline().split())
A = list(map(int, readline().split()))
S = sum(A)
data = set()
data.add(0)
s = 0
result = 0
if S == K:
    result += 1
for a in A:
    s += a
    key = K - S + s
    result += key in data
    data.add(s)
print(result)
