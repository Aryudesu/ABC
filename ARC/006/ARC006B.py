N, L = [int(l) for l in input().split()]
LN = [i + 1 for i in range(N)]
for l in range(L):
    S = input()
    for n in range(N - 1):
        if S[2 * n + 1] == "-":
            LN[n], LN[n + 1] = LN[n + 1], LN[n]
            # print(LN)
G = input()
for n in range(N):
    if G[2 * n] == "o":
        print(LN[n])
