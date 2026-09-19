N, M, K = map(int, input().split())
data = [["#"] * M for _ in range(N)]
for k in range(K):
    r, c = map(int, input().split())
    data[r-1][c-1] = "."
for dat in data:
    print("".join(dat))
