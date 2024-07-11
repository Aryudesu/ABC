N, Q = [int(l) for l in input().split()]
S = input()
data = [0]
c = 0
for i in range(1, N):
    if S[i-1] == S[i]:
        c += 1
    data.append(c)
result = []
for q in range(Q):
    l, r = [int(l) - 1 for l in input().split()]
    result.append(data[r] - data[l])
for r in result:
    print(r)
