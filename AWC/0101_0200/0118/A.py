N, M = map(int, input().split())
data = [set() for _ in range(M)]
for n in range(N):
    S = list(map(int, input().split()))
    for m in range(M):
        if S[m] != -1:
            data[m].add(S[m])
isOk = True
for dat in data:
    if len(dat) > 1:
        isOk = False
        break
print("Yes" if isOk else "No")
