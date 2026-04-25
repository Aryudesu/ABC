from itertools import product
from typing import Tuple

def makeData(data: list[Tuple[int, int, int]], target: int)->set[int]:
    result = set()
    N = len(data)
    for dat in product([0, 1, 2], repeat=N):
        num = 0
        f = True
        for i in range(N):
            num += data[i][dat[i]]
            if num > target:
                f = False
                break
        if f:
            result.add(num)
    return result


def calc(dataA: set[int], dataB: set[int], target: int)->bool:
    for a in dataA:
        if target - a in dataB:
            return True
    return False

# いくつか選ぶんだぁぁぁぁ・・・
N, K = map(int, input().split())
data = []
for n in range(N):
    a, b = map(int, input().split())
    data.append((a, b, 0))
mid = N//2
datA = makeData(data[:mid], K)
datB = makeData(data[mid:], K)
print("Yes" if calc(datA, datB, K) else "No")
# 祝☆全完
