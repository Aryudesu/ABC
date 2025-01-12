def calc(N, k, TL):
    max_data = TL[0][0] * (TL[0][1] + k)
    for n in range(1, N):
        t, l = TL[n]
        max_data = max([t * (l + k), max_data])
    return max_data


N, D = [int(l) for l in input().split()]
TL = []
for n in range(N):
    TL.append([int(l) for l in input().split()])
for k in range(1, D + 1):
    print(calc(N, k, TL))
