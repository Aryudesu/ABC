from itertools import product

N = int(input())
L = list(map(int, input().split()))
result = 0
for dir in product((1, -1), repeat=N):
    res = 0
    now = 1
    prev = 1
    for idx in range(N):
        prev = now
        l = L[idx] * 2
        now += dir[idx] * l
        if prev * now < 0:
            res += 1
    result = max(res, result)
print(result)
