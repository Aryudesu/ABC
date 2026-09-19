from bisect import bisect_right
N, V, Q = map(int, input().split())
# 時間
T = [0]
W = [0]
# 時間開始時の位置
pos = [0]
for n in range(N):
    t, w = map(int, input().split())
    T.append(t)
    if w == 0:
        W.append(w)
    elif w < 0:
        W.append(w - V)
    elif w > 0:
        W.append(w + V)
    if W[-2] == 0:
        pos.append(pos[-1])
    elif W[-2] < 0:
        pos.append(pos[-1] + W[-2] * (T[-1] - T[-2]))
    elif W[-2] > 0:
        pos.append(pos[-1] + W[-2] * (T[-1] - T[-2]))
# print(T)
# print(W)
# print(pos)
result = []
for _ in range(Q):
    X = int(input())
    idx = bisect_right(T, X) - 1
    result.append(pos[idx] + W[idx] * (X - T[idx]))
print(*result, sep="\n")
