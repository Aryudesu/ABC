from heapq import heappop, heappush

MAX = 10 ** 9
s = 1
beki = []
data = []
memo = set()
while s <= MAX:
    heappush(data, s)
    beki.append(s)
    memo.add(s)
    s <<= 1
N = int(input())
for n in range(N-1):
    num = heappop(data)
    for b in beki:
        tmp = num * (10 ** len(str(b))) + b
        if tmp <= MAX and tmp not in memo:
            heappush(data, tmp)
            memo.add(tmp)
        tmp = b * (10 ** len(str(num))) + num
        if tmp <= MAX and tmp not in memo:
            heappush(data, tmp)
            memo.add(tmp)
print(heappop(data))
