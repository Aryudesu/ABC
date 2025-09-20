N, R = [int(l) for l in input().split()]
L = [int(l) for l in input().split()]
# 空いてるフラグ
lf = False
result = 0
for i in range(R):
    if L[i] == 1 and lf:
        # 左端から空いている扉があって，閉まっている扉があるなら開けて閉めて戻るから2回
        result += 2
    elif L[i] == 0:
        # 空いているものは閉める
        lf = True
        result += 1
lf = False
for i in range(N, R, -1):
    if L[i-1] == 1 and lf:
        # 左端から空いている扉があって，閉まっている扉があるなら開けて閉めて戻るから2回
        result += 2
    elif L[i-1] == 0:
        # 空いているものは閉める
        lf = True
        result += 1
print(result)
