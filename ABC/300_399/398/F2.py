S = input()
N = len(S)
for i in range(N):
    ok = True
    for j in range(i, N):
        k = N - 1 + i - j
        if S[j] != S[k]:
            ok = False
            break
        if j >= k:
            break
    if ok:
        for j in range(N + i):
            print(S[min(j, N + i - 1 - j)], end="")
        print()
        break
