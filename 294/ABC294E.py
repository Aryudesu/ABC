L, N1, N2 = [int(l) for l in input().split()]
VL1 = []
for n1 in range(N1):
    VL1.append([int(l) for l in input().split()])
VL2 = []
for n2 in range(N2):
    VL2.append([int(l) for l in input().split()])
# 注目圧縮場所
i1 = 0
# 余った圧縮
r1 = 0
# 注目圧縮場所
i2 = 0
# 余った圧縮
r2 = 0
result = 0
while i1 < N1 and i2 < N2:
    # 長さ
    v1 = VL1[i1][1] - r1
    v2 = VL2[i2][1] - r2
    n1 = VL1[i1][0]
    n2 = VL2[i2][0]
    if v1 > v2:
        if n1 == n2:
            result += v2
        r1 += v2
        r2 = 0
        i2 += 1
    elif v1 < v2:
        if n1 == n2:
            result += v1
        r2 += v1
        r1 = 0
        i1 += 1
    else:
        if n1 == n2:
            result += v1
        r1 = 0
        r2 = 0
        i1 += 1
        i2 += 1
print(result)
