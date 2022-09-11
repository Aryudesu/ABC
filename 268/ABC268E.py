N = int(input())
p = [int(l) for l in input().split()]

data = [0] * N
for n in range(N):
    data[(p[n] - n) % N] += 1

# 計算開始地点
MI = 0
for n in range(N):
    if data[MI] < data[n]:
        MI = n

# 計算終了地点
LE = (N + 1)//2 if N % 2 else N // 2
print(data)
print(MI)
res = 0
# 左右に計算していく
for le in range(1, LE):
    res += le * (data[(MI + le) % N] + data[(MI - le) % N])
# 最後の計算
if N % 2 == 0:
    res += LE * data[(MI + LE) % N]
print(res)
