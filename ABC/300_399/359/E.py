from collections import deque

N = int(input())
H = [int(l) for l in input().split()]
# スタックデータ
Data = deque()
Data.append(10**10)
W = deque()
W.append(1)
R = deque()
R.append(0)
result = []
for idx in range(N):
    h = H[idx]
    W.append(1)
    while Data[-1] < h:
        Data.pop()
        w = W.pop()
        R.pop()
        W[-1] += w
    Data.append(h)
    R.append(R[-1] + Data[-1] * W[-1])
    result.append(R[-1] + 1)
    # print("Data", Data)
    # print("W", W)
    # print("R", R)
print(*result)
