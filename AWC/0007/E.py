from typing import Tuple

def num2xy(N: int, num: int)->Tuple[int, int]:
    num -= 1
    x, y = num % N, num // N
    return (x, y)

N, M = map(int, input().split())
S, T = map(int, input().split())
# スタートとゴール
sx, sy = num2xy(N, S)
tx, ty = num2xy(N, T)
if M == 0:
    print(abs(sx - tx) + abs(sy - ty))
    exit()

P = list(map(int, input().split()))
# print("debug", sx, sy, tx, ty)
# 各点の距離
weight = [[0] * M for _ in range(M)]
for i in range(M):
    for j in range(M):
        p1, p2 = P[i], P[j]
        x1, y1 = num2xy(N, p1)
        x2, y2 = num2xy(N, p2)
        weight[i][j] = abs(x1 - x2) + abs(y1 - y2)

# 多分bit全探索(いま居る町, 到達した町) = 最小距離
dp = dict()
# スタートから移動
for i in range(M):
    p = P[i]
    x, y = num2xy(N, p)
    dp[(1 << i, i)] = abs(sx - x) + abs(sy - y)
MAX = 10 ** 10
for _ in range(M-1):
    nextDP = dict()
    for key in dp:
        dist = dp[key]
        bitData, num = key
        for i in range(M):
            b = 1 << i
            if bitData & b != 0:
                continue
            # 新しく到達するところ
            newBit = bitData | b
            newDist = dist + weight[num][i]
            # 移動
            nextDP[(newBit, i)] = min(newDist, nextDP.get((newBit, i), MAX))
    dp = nextDP
# print(dp)
result = MAX
for key in dp:
    bitData, num = key
    dist = dp[key]
    x, y = num2xy(N, P[num])
    result = min(result, dist + abs(tx - x) + abs(ty - y))
print(result)
