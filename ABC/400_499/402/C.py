from collections import defaultdict

N, M = [int(l) for l in input().split()]
data = defaultdict(set)
for m in range(M):
    K, *A = [int(l) for l in input().split()]
    for a in A:
        data[a].add(m + 1)
B = [int(l) for l in input().split()]
B.reverse()
memo = set()
cnt = 0
result = []
for b in B:
    cnt = M - len(memo)
    result.append(cnt)
    memo.update(data[b])
result.reverse()
for r in result:
    print(r)
