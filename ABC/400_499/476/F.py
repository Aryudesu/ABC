N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
field = [[0] * N for _ in range(N)]
zerozero = 0
for h in range(N):
    for w in range(N):
        num = (A[h] * B[w]) % M
        field[h][w] = num
        zerozero += num * max(h, w)
print(zerozero)
