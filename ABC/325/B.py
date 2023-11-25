N = int(input())
data = [0] * 24
for n in range(N):
    W, X = [int(l) for l in input().split()]
    for t in range(9):
        data[(9 - X + t) % 24] += W
print(max(data))
