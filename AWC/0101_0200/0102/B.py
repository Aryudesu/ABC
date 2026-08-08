from bisect import bisect_right

N, M = map(int, input().split())
R = list(map(int, input().split()))
S = list(map(int, input().split()))
R.sort()
result = 10 ** 18
for s in S:
    result = min(result, bisect_right(R, s))
print(result)
