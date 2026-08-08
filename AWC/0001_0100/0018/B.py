from collections import defaultdict

N, M = map(int, input().split())
C = list(map(int, input().split()))
result = 0
for n in range(N):
    data = defaultdict(int)
    K = int(input())
    P = list(map(int, input().split()))
    for p in P:
        data[p-1] += 1
    for m in data:
        if C[m] >= data[m]:
            result += data[m]
print(result)
