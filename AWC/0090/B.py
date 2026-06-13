from typing import Tuple

def calc(L: int, N: int, C: int, PW: list[Tuple[int, int]]):
    prev = 0
    power = C
    for p, w in PW:
        if p - prev > power:
            return -1
        power = min(C, power - (p - prev) + w)
        prev = p
    if L - prev > power:
        return -1
    power = power - (L - prev)
    return power

L, N, C = map(int, input().split())
PW = []
for n in range(N):
    p, w = map(int, input().split())
    PW.append((p, w))
print(calc(L, N, C, PW))
