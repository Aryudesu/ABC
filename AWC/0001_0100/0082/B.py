def proc(num: int, K: int, N: int)->int:
    res = num
    b = (1 << (N-1))
    for k in range(K):
        if res & 1:
            return res
        res >>= 1
        res |= b
    return res

def calc(num: int, Y: list[int], N: int, M: int)->int:
    result = 0
    lYData = Y.copy()
    lYData.append(num)
    rYData = [0] * (M + 1)
    b = 1
    for n in range(N-1):
        tmp = 0
        for m in range(M + 1):
            y = lYData[m]
            lYData[m] = y >> 1
            if y & 1:
                rYData[m] += b
            tmp += lYData[m] + rYData[m]
        b <<= 1
        # print(lYData, rYData)
        result = max(result, tmp)
    return result

N, K, M, X = map(int, input().split())
if M > 0:
    Y = list(map(int, input().split()))
else:
    Y = []
print(calc(proc(X, K, N), Y, N, M))
