from itertools import permutations
from typing import Tuple

def isOk(nums: Tuple[int], N: int, K: int)-> bool:
    # 順列に対して置換がK回行われたか判定したい
    tNums = list(nums)
    data = dict()
    for i in range(N):
        data[tNums[i]] = i
    count = 0
    for i in range(N):
        # iが入っているindexを取得する
        idx = data[i]
        # 正しい場所にあったらスルー
        if i == idx:
            continue
        # 正しい位置にある数値を取得する
        n = tNums[i]
        # swapしたい
        tNums[i] = i
        tNums[idx] = n
        data[n] = idx
        count += 1
        # print(nums, tNums, count)
    return count <= K

N, K = map(int, input().split())
C = []
for n in range(N):
    C.append(list(map(int, input().split())))

result = 0
for dat in permutations(range(N)):
    if not isOk(dat, N, K):
        continue
    # print(dat)
    tmp = 0
    for i in range(N):
        a, b = dat[i], dat[i-1]
        tmp += C[a][b]
    result = max(result, tmp)
print(result)

# ALL AC~~~!!!
