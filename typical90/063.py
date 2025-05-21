from collections import defaultdict
from itertools import product

H, W = [int(l) for l in input().split()]
P = []
for h in range(H):
    P.append([int(l) for l in input().split()])

result = 0
for bits in product([0, 1], repeat=H):
    nums = defaultdict(lambda: 0)
    for w in range(W):
        tmp = set()
        count = 0
        for h in range(H):
            if bits[h] != 0:
                count += 1
                tmp.add(P[h][w])
        if len(tmp) == 1:
            n = tmp.pop()
            nums[n] += count
            result = max(result, nums[n])
print(result)
