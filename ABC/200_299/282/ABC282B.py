N, M = [int(l) for l in input().split()]
S = []
for n in range(N):
    S.append(input())
result = 0
for n1 in range(N - 1):
    for n2 in range(n1 + 1, N):
        f = True
        for m in range(M):
            if S[n1][m] == "x" and S[n2][m] == "x":
                f = False
                break
        if f:
            result += 1
print(result)
