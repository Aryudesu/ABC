from typing import Tuple

def calcBW(N: int, M: int)->Tuple[int, int]:
    N2 = N - (N & 1)
    M2 = M - (M & 1)
    base = N2 * M2
    B, W = base // 2, base // 2
    if N & 1:
        B += M2 // 2
        W += M2 // 2
    if M & 1:
        B += N2 // 2
        W += N2 // 2
    if (N & 1) and (M & 1):
        B += 1
    return B, W

N, M, K = map(int, input().split())
B, W = calcBW(N, M)
BC = []
for _ in range(K):
    b, c = map(int, input().split())
    BC.append((b, c))
BC.sort()
result = 0
B, W = max(B, W), min(B, W)
while BC:
    if not B and not W:
        break
    b, c = BC.pop()
    if B >= c:
        B -= c
        result += b * c
    else:
        B, W = max(B, W), min(B, W)
        if B >= c:
            result += b * c
            B -= c
        else:
            result += b * B
            B = 0

