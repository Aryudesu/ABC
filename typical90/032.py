import itertools

N = int(input())
A = []
INF = 3000000
for n in range(N):
    A.append([int(l) for l in input().split()])
M = int(input())
bad = set()
for m in range(M):
    x, y = [int(l) - 1 for l in input().split()]
    bad.add((x, y))
    bad.add((y, x))

result = INF
# itr[どこの区間を] = 誰が走るか
for itr in itertools.permutations(list(range(N))):
    res = 0
    bf = False
    for j in range(N):
        i = itr[j]
        res += A[i][j]
        if j > 0:
            if (itr[j], itr[j-1]) in bad:
                bf = True
                break
    if not bf and result > res:
        result = res
print(-1 if result == INF else result)
