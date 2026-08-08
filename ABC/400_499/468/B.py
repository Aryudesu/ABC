M, D = map(int, input().split())
S = input()
data = [0] * M
c = 0
for m in range(M):
    if S[m] == "G":
        c = D + 1
    data[m] = c
    c = max(c-1,0)
c = 0
for m in range(M):
    if S[-1-m] == "G":
        c = D + 1
    data[-1-m] = max(c, data[-1-m])
    c = max(c-1,0)
print(data.count(0))
