H, W = [int(l) for l in input().split()]
S = [[0 for _ in range(H)] for _ in range(W)]
T = [[0 for _ in range(H)] for _ in range(W)]
for h in range(H):
    tmp = input()
    for w in range(W):
        S[w][h] = tmp[w]
for h in range(H):
    tmp = input()
    for w in range(W):
        T[w][h] = tmp[w]
S.sort()
T.sort()
print("Yes" if S == T else "No")
