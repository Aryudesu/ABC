# 与えられたターン数で実現可能かどうか
def feasibility(TD, H, turn):
    pass


N, H = [int(l) for l in input().split()]
max_d = 0
# 効率が良いものを選別
DT = dict()
for n in range(N):
    t, d = [int(l) for l in input().split()]
    tmp = DT.get(d, 0)
    if tmp < t:
        DT[d] = t
    if d > max_d:
        max_d = d
TD = dict()
for d in DT:
    t = DT[d]
    tmp = TD.get(t, 0)
    if tmp < d:
        TD[t] = d
# 愚直最大ターン
max_turn = H // max_d + (1 if H % max_d else 0)

# 二分探索を行いたい
r = max_turn
l = 0
while True:
    m = (l + r) // 2
    if feasibility(TD, H, m):
        r = m
    else:
        l = m
    if l + 1 >= r:
        break
print(l)
