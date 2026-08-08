from typing import Tuple
def calc(H: int, M: int)->Tuple[int, int, int]:
    resM = M % 60
    resH = H + M // 60
    return (resH // 24, resH % 24, resM)

N = int(input())
for _ in range(N):
    H, M = map(int, input().split())
    D, H, M = calc(H, M)
    print(D, H, M)
