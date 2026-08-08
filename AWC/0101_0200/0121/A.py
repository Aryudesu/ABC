N, M = map(int, input().split())
D = list(map(int, input().split()))
dMax = max(D)
result = 0
for m in range(M):
    s, h = input().split()
    result += dMax < int(h)
print(result)
