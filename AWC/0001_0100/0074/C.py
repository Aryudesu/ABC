N, M = map(int, input().split())
switchCount = [0] * (N + 1)
for m in range(M):
    l, r = map(int, input().split())
    switchCount[l-1] += 1
    switchCount[r] -= 1
count = 0
result = 0
for i in range(N):
    count += switchCount[i]
    if count % 2 == 1:
        result += 1
print(result)
