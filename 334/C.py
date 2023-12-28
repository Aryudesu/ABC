def calcOdd(N, K, A):
    data = []
    for i in range(K-1):
        data.append(abs(A[i + 1] - A[i]))
    if len(data) == 0:
        return 0
    p = len(data) - 2
    s = 0
    idx = 0
    while idx <= p:
        s += data[idx]
        idx += 2
    result = s
    idx = p
    while idx >= 0:
        s = s - data[idx]
        s += data[idx + 1]
        if s < result:
            result = s
        idx -= 2
    return result


def calcEven(N, K, A):
    result = 0
    for i in range(K // 2):
        result += abs(A[i * 2] - A[i * 2 - 1])
    return result

N, K = [int(l) for l in input().split()]
A = [int(l) for l in input().split()]
if K % 2 == 0:
    print(calcEven(N, K, A))
else:
    print(calcOdd(N, K, A))
