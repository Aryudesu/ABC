N, M = [int(l) for l in input().split()]
result = 0
memo = set()
for m in range(M):
    u, v = [int(l) - 1 for l in input().split()]
    tmp1 = tuple([u, v])
    tmp2 = tuple([v, u])
    if tmp1 in memo or tmp2 in memo or u == v:
        result += 1
    memo.add(tmp1)
    memo.add(tmp2)
print(result)
