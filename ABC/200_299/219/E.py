from atcoder.dsu import DSU
from itertools import product

def check(data: tuple[int], A: list[int], lastOne: int)-> bool:
    dsu = DSU(17)
    outer = 16
    # 堀外部について
    for i in range(4):
        if data[i] == 0:
            dsu.merge(outer, i)
        if data[i+12] == 0:
            dsu.merge(outer, i+12)
        if data[i*4] == 0:
            dsu.merge(outer, i*4)
        if data[i*4 + 3] == 0:
            dsu.merge(outer, i*4 + 3)
    # 堀内部について
    for i in range(16):
        if A[i] == 1 and data[i] == 0:
            return False
        if i % 4 != 3 and data[i+1] == data[i]:
            dsu.merge(i, i+1)
        if i < 12 and data[i+4] == data[i]:
            dsu.merge(i, i+4)
    # チェック
    oneLeader = dsu.leader(lastOne)
    for i in range(16):
        if data[i] == 1:
            if dsu.leader(i) != oneLeader:
                return False
        elif data[i] == 0:
            if A[i] == 1:
                return False
            if not dsu.same(i, outer):
                return False
    return True

A = []
c = 0
# Aには必ず1が存在するので甘えておく
lastOne = 0
for i in range(4):
    tmp = list(map(int, input().split()))
    for t in tmp:
        A.append(t)
        if t == 1:
            lastOne = c
        c += 1
result = 0
for data in product([0, 1], repeat=16):
    if check(data, A, lastOne):
        result += 1
print(result)
