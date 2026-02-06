H, W, N = map(int, input().split())
A = []
for h in range(H):
    A.append(list(map(int, input().split())))
B = set()
for n in range(N):
    B.add(int(input()))
result = 0
for h in range(H):
    tmp = 0
    for w in range(W):
        if A[h][w] in B:
            tmp += 1
    result = max(tmp, result)
print(result)
