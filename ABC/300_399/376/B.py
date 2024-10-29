N, Q = [int(l) for l in input().split()]
L, R = 0, 1
result = 0
for q in range(Q):
    h, t = [l for l in input().split()]
    t = int(t) - 1
    if h == "L":
        lh = (L - L) % N
        rh = (R - L) % N
        th = (t - L) % N
        if th >= rh and rh >= lh:
            result += N - th
        else:
            result += th
        L = t
    elif h == "R":
        rh = (R - R) % N
        lh = (L - R) % N
        th = (t - R) % N
        if th >= lh and lh >= rh:
            result += N - th
        else:
            result += th
        R = t
    else:
        raise Exception()
    # print(result, L, R)
print(result)
