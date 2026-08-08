from typing import Tuple

def calc(data: list[Tuple[int, int]], K: int)->int:
    if len(data) == 0:
        return 0
    result = 0
    for idx in range(len(data)):
        x, d = data[idx]
        if d % K == 0:
            result += (d // K) * x
            data[idx][1] = 0
    for idx in range(len(data) - 1, 0, -1):
        x, d = data[idx]
        data[idx] = None
        if d == 0:
            continue
        result += (d // K) * x
        d1 = d % K
        if d1 and idx > 0:
            _, d2 = data[idx - 1]
            if d1 + d2 > K:
                data[idx - 1][1] = d1 + d2 - K
                result += x
            else:
                data[idx - 1][0] = x
                data[idx - 1][1] = d1 + d2
    if data[0][1] > 0:
        result += ((data[0][1] + K - 1)//K)*data[0][0]
    return result


N, K = map(int, input().split())
PXD = []
MXD = []
for n in range(N):
    x, d = map(int, input().split())
    if x > 0:
        PXD.append([x, d])
    else:
        MXD.append([-x, d])

PXD.sort()
MXD.sort()

print((calc(PXD, K) + calc(MXD, K)) * 2)
