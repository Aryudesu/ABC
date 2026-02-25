H, W, K = map(int, input().split())
c1, c2 = input().split()
for h in range(H):
    S = input()
    tmp = ""
    for w in range(W*K):
        tmp += c1 if S[w//K] == "#" else c2
    for k in range(K):
        print(tmp)
