import bisect


def calc(N, M, D, A, B):
    for a in A:
        res = 0
        tmp1 = bisect.bisect_left(B, a)
        for i in range(-1, 2):
            if tmp1 + i >= M:
                continue
            if abs(B[tmp1 + i] - a) <= D:
                if a + B[tmp1 + i] > res:
                    res = a + B[tmp1 + i]
        tmp2 = bisect.bisect_right(B, a + D)
        for i in range(-1, 2):
            if tmp2 + i >= M:
                continue
            if abs(B[tmp2 + i] - a) <= D:
                if a + B[tmp2 + i] > res:
                    res = a + B[tmp2 + i]
        if res != 0:
            return res
    return None


N, M, D = [int(l) for l in input().split()]
A = [int(l) for l in input().split()]
B = [int(l) for l in input().split()]
A.sort(reverse=True)
B.sort()
res = calc(N, M, D, A, B)
print(res if res else -1)
