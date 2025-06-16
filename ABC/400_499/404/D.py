from itertools import product

N, M = [int(l) for l in input().split()]
C = [int(l) for l in input().split()]

zooData = [list() for _ in range(N)]
for m in range(M):
    K, *A = [int(l) - 1 for l in input().split()]
    # 動物園iで見ることができる動物達
    for a in A:
        zooData[a].append(m)

result = 10 ** 13
# 各動物園についてそれぞれ何回訪れたか
for data in product([0, 1, 2], repeat = N):
    # 動物を見た階数
    couter = [0] * M
    # この場合の料金
    res = 0
    for i in range(N):
        # その動物園の値段 * 行った回数
        res += C[i] * data[i]
        for a in zooData[i]:
            couter[a] += data[i]
    isok = True
    for m in couter:
        if m < 2:
            isok = False
            break
    if isok:
        result = min(result, res)
print(result)
