def calc(S, N):
    Slen = len(S)
    maxS = 0
    minS = 0
    qs = set()
    tmp = 1
    for s in S:
        if s == "0":
            maxS *= 2
            minS *= 2
        elif s == "1":
            minS = minS * 2 + 1
            maxS = maxS * 2 + 1
        elif s == "?":
            minS *= 2
            maxS = maxS * 2 + 1
            qs.add(tmp)
        tmp *= 2
    diff = maxS - N
    if N < minS:
        return -1
    elif maxS == N:
        return maxS
    elif minS == N:
        return minS
    dp = set([0])
    max_data = 10 ** 10
    for q in qs:
        new_dp = set()
        for d in dp:
            new_dp.add(d)
            if q + d <= max_data:
                if q + d >= diff:
                    max_data = q + d
                new_dp.add(q + d)
        dp = new_dp
    max_min = 10**10
    for d in dp:
        if d > diff and max_min > d:
            max_min = d
    return maxS - max_min


S = input()
N = int(input())
print(calc(S, N))
