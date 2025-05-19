def calc(N, P):
    up_count = 0
    dn_count = 0
    data = []
    data.append(0)
    for i in range(1, N - 1):
        if P[i-1] > P[i] and P[i] < P[i+1]:
            data.append(-1)
            dn_count += 1
        elif P[i-1] < P[i] and P[i]  > P[i+1]:
            data.append(1)
            up_count += 1
        else:
            data.append(0)
    if up_count == 0 or dn_count == 0:
        return 0
    data.append(0)
    l = 0
    r = -1
    c = 0
    for i in range(N):
        if data[i] != 0:
            c += 1
        if c == 3:
            r = i
            break

N = int(input())
P = [int(l) for l in input().split()]

