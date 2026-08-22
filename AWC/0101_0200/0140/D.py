def calc(data: list[int])->int:
    if len(data) == 1:
        return 1
    first = 0
    second = 0
    N = len(data)
    for i in range(1, N):
        d = data[i] - data[i-1]
        if d >= first:
            second = first
            first = d
        elif d >= second:
            second = d
    l = first//2
    r = first - l
    return max(l, r, second)

N, M = map(int, input().split())
S = list(map(int, input().split()))
S.sort()
res1 = calc(S[1:])
res2 = calc(S[:-1])
print(min(res1, res2))
