import heapq

N, K = [int(l) for l in input().split()]
S = input()
sArr = []
for i in range(N):
    sArr.append((S[i], i))
sArr.sort()

data = [s for s in sArr]
memo = []
res = []
hpq = heapq.heapify(data)
count = 0
while count < N - K + 1:
    for k in range(K):
        tmp = heapq.heappop(data)
        res.append(tmp[0])
        memo.append(tmp[0])
    memo = []
    count += 1
