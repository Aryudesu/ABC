from itertools import permutations
from typing import Tuple

def isOk(UV: list[Tuple[int, int]], idxData: dict[int, int])->int:
    for u, v in UV:
        if idxData[u] > idxData[v]:
            return False        
    return True


N, M = map(int, input().split())
A = list(map(int, input().split()))
UV = []
if M > 0:
    for m in range(M):
        u, v = map(int, input().split())
        UV.append((u-1, v-1))

result = 0
for data in permutations(range(N)):
    idxData = dict()
    # idxData[その社員が] = 何番目に発表するか
    for idx in range(N):
        idxData[data[idx]] = idx
    if isOk(UV, idxData):
        tmp = 0
        for idx in range(N):
            tmp += A[data[idx]] * (1 + idx)
        result = max(result, tmp)
        # print(data)
print(result)
