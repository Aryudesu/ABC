def calc(N):
    sq = [False for i in range(N+1)]
    c = 1
    while c**2 <= N:
        sq[c**2] = True
        c+=1
    d = [[] for l in range(N+1)]
    for i in range(1, N+1):
        for j in range(i, N+1, i):
            d[j].append(i)
    cnt = [0 for l in range(N+1)]
    for i in range(1, N+1):
        f = 0
        for j in range(len(d[i])):
            if sq[d[i][j]]:
                f = d[i][j]
        cnt[i//f] += 1
    ans = 0
    for c in cnt:
        ans += c**2
    print(ans)


N = int(input())
calc(N)
