from typing import Tuple

def calc(ARV: list[Tuple[int, int, int]], t: int, s: int, p: int)-> int:
    result = 1
    l = s - 1
    r = s - 1
    while True:
        a, r, v = ARV[l]

N, L, Q = map(int, input().split())
ARV = []
for n in range(N):
    a, r, v = map(int, input().split())
    ARV.append((a, r, v))

for _ in range(Q):
    t, s, p = map(int, input().split())

