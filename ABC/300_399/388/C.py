from bisect import bisect_left

N = int(input())
A = [int(l) for l in input().split()]
result = 0
for a in A:
    tmp = bisect_left(A, a * 2)
    if tmp < N:
        result += (N - tmp)
print(result)
