from collections import defaultdict

colors = defaultdict(int)
N = int(input())
C = list(map(int, input().split()))
maxC = 0
for c in C:
    colors[c] += 1
    if colors[maxC] < colors[c]:
        maxC = c
print(N - colors[maxC])
