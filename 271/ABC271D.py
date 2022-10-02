# 通ってください
N, S = [int(l) for l in input().split()]
ab = []
for n in range(N):
    ab.append([int(l) for l in input().split()])
RS = 'HT'
for k in range(2**N):
    tmp = k
    s = 0
    r = []
    for n in range(N):
        s += ab[n][tmp&1]
        r.append(RS[tmp&1])
        tmp = tmp >> 2
        if s > S:
            break
    if s == S:
        break
if s == S:
    print('Yes')
    print(''.join(r))
else:
    print('No')
