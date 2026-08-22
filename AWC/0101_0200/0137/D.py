H, W, N = map(int, input().split())
data = set()
for n in range(N):
    r, c = map(int, input().split())
    data.add((r - min(r, c) - 1, c - min(r, c) - 1))
print(len(data))
