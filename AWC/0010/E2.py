from itertools import permutations
from typing import Tuple

def calcReplacementNum(arr: Tuple[int], N: int)-> int:
    """配列が何回置換が行われた結果できるのか計算します"""
    tNums = list(arr)
    # 現在の位置に何の数字があるかを保存する
    data = dict()
    for i in range(N):
        data[tNums[i]] = i
    # 位置を入れ替えていく
    result = 0
    for i in range(N):
        idx = data[i]
        if i == idx:
            continue
        n = tNums[i]
        tNums[i], tNums[idx] = i, n
        data[i], data[n] = i, idx
        result += 1
    return result

# === AWC0010E

N, K = map(int, input().split())
C = []
for n in range(N):
    C.append(list(map(int, input().split())))

result = 0
for dat in permutations(range(N)):
    if calcReplacementNum(dat, N) > K:
        continue
    tmp = 0
    for i in range(N):
        a, b = dat[i], dat[i-1]
        tmp += C[a][b]
    result = max(result, tmp)
print(result)

