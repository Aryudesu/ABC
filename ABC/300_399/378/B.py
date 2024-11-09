N = int(input())
QR = []
for n in range(N):
    QR.append([int(l) for l in input().split()])
Q = int(input())
result = []
for _ in range(Q):
    t, d = [int(l) for l in input().split()]
    q, r = QR[t - 1]
    if d % q == r:
        result.append(d)
    elif d % q > r:
        tmp = d // q + 1
        result.append(tmp * q + r)
    else:
        tmp = d // q
        result.append(tmp * q + r)
for r in result:
    print(r)
