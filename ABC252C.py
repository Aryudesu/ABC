N = int(input())
data = []
for n in range(N):
    S = input()
    tmp = [0] * 10
    for s in range(len(S)):
        t = int(s)
        c = 0
        for dat in data:
            if dat[int(S[s])] % 10 == s:
                c += 1
        tmp[int(S[s])] = s + 10 * c
    data.append(tmp)
Min = 10 * N
for n in range(10):
    max = 0
    for dat in data:
        if max < dat[n]:
            max = dat[n]
    if Min > max:
        Min = max
print(Min)
