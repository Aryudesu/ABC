N = int(input())
S = [int(l) for l in input().split()]
T = [int(l) for l in input().split()]
# その人に宝石が渡る最短時間
Sunuke = [0] * N
index = 0
# 一旦渡される時間で初期化しておく
for i in range(N):
    Sunuke[i] = T[i]
    if T[index] > T[i]:
        index = i
for i in range(N):
    idx1 = (index + i) % N
    idx2 = (index + i + 1) % N
    Sunuke[idx2] = min(Sunuke[idx2], Sunuke[idx1] + S[idx1])
for s in Sunuke:
    print(s)
