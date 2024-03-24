N = int(input())
S = input()
T = input()
P = []
eql = []
S1 = 0
T1 = 0
diff = 0
for n in range(N):
    d = S[n] == T[n]
    P.append(d)
    if not d:
        diff += 1
    else:
        eql.append(S[n])
    if S[n] == '1':
        S1 += 1
    if T[n] == '1':
        T1 += 1
if diff % 2:
    print(-1)
    exit()
if S1 == T1:
    print('0' * N)
    exit()
res = []
co = 0
if T1 > S1:
    S = T
eql.sort()
eqc = 0
for n in range(N):
    if P[n]:
        res.append('0')
    else:
        if co < diff//2 and S[n] == '1':
            res.append('0')
            co += 1
        else:
            res.append(S[n])
print(''.join(res))
