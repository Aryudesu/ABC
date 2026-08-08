N, L, R = map(int, input().split())
T = list(map(int, input().split()))
result = 0
count = 0
for t in T:
    if L <= t <= R:
        count += 1
    else:
        count = 0
    result = max(result, count)
print(result)
