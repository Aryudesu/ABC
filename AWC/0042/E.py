from atcoder.dsu import DSU

def calc(N: int, K: int, M: int, A: list[int])->int:
    """うまいくいかない解法"""
    dsu = DSU(N)
    data = []
    flag = [False] * N
    for i in range(N):
        data.append((A[i], i))
    data.sort(reverse=True)
    result = 0
    for a, idx in data:
        sizeL = 0
        sizeR = 0
        if idx - 1 >= 0 and flag[idx - 1]:
            sizeL = dsu.size(idx-1)
        if idx + 1 < N and flag[idx + 1]:
            sizeR = dsu.size(idx+1)
        if sizeL + sizeR + 1 < K:
            if idx - 1 >= 0 and flag[idx - 1]:
                dsu.merge(idx-1, idx)
            if idx + 1 < N and flag[idx + 1]:
                dsu.merge(idx+1, idx)
            result += a
            flag[idx] = True
        print(flag)
    return result


N, K, M = map(int, input().split())
A = list(map(int, input().split()))
res = calc(N, K, M, A)
print(res)
# [12] 5 [8 20] 3 [15] 7 [11 9 18] 6 [14] 2 [10 16] -> 133 orz
