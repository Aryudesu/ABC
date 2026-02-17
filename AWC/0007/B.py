N, K = map(int, input().split())
count = 0
comp = dict()
data = []
M = []
for n in range(N):
    M.append(int(input()))
    W = input().split()
    dat = set()
    for w in W:
        if not w in comp:
            comp[w] = count
            count += 1
        dat.add(comp[w])
    data.append(dat)
result = 0
for i in range(N-1):
    for j in range(i+1, N):
        k = 0
        m1, m2 = M[i], M[j]
        dat1, dat2 = data[i], data[j]
        if m1 > m2:
            m1, m2 = m2, m1
            dat1, dat2 = dat2, dat1
        for d in dat1:
            if d in dat2:
                k += 1
                if k >= K:
                    result += 1
                    break
print(result)
