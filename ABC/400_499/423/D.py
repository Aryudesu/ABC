from collections import deque
from heapq import heappop, heappush, heapify

N, K = [int(l) for l in input().split()]
idx = 0
# 入店人数（出ていく時間順）
data = []
heapify(data)
# 待ち人数
machi = deque()
# 入店人数
inNum = 0
# 現在時刻
now = 0
result = dict()
for n in range(N):
    a, b, c = [int(l) for l in input().split()]
    machi.append((a, b, c, n))

for n in range(N):
    a, b, c, idx = machi.popleft()
    while True:
        # 客が捌けていれば入店
        if inNum + c <= K:
            # 現在時刻更新
            if now < a:
                now = a
            inNum += c
            heappush(data, (now + b, c))
            result[idx] = now
            break
        # 退店時刻, 人数
        t, u = heappop(data)
        if now < t:
            now = t
        inNum -= u
for i in range(N):
    print(result[i])
