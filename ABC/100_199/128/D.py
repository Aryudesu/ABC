from heapq import heappop, heappush

def calc(V: list[int], a: int, b: int, c: int)->int:
    s = 0
    data = []
    for i in range(a):
        s += V[i]
        heappush(data, V[i])
    for i in range(b):
        s += V[-(1+i)]
        heappush(data, V[-(1+i)])
    for i in range(c):
        t = heappop(data)
        s -= t
    return s

N, K = map(int, input().split())
V = list(map(int, input().split()))
result = -(10**18)
for M in range(K + 1):
    # k回取り出す
    for k in range(M + 1):
        if N < k:
            continue
        # c回入れる
        c = M - k
        if k < c:
            continue
        # 左からa回取り出す
        for a in range(k + 1):
            # 右からb回取り出す
            b = k - a
            res = calc(V, a, b, c)
            result = max(result, res)
print(result)
