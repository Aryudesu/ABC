from sortedcontainers import SortedList
from collections import defaultdict
from atcoder.dsu import DSU

N, K, Q = map(int, input().split())
A = []
B = []
for _ in range(K):
    a, b = map(int, input().split())
    A.append(a)
    B.append(b)
for _ in range(Q):
    x, p, v = map(int, input().split())
    if x == 1:
        a = A[p-1]
        A[p-1] = v
    elif x == 2:
        b = B[p-1]
        B[p-1] = v
    else:
        raise ValueError()
    C = sorted(A)
    D = sorted(B)
    dsu = DSU(2*K)
    nums = dict()
    c = 0
    for k in range(K):
        if C[k] not in nums:
            nums[C[k]] = c
            c += 1
        if D[k] not in nums:
            nums[D[k]] = c
            c += 1
        if C[k] != D[k]:
            dsu.merge(nums[C[k]], nums[D[k]])
    res = []
    for k in range(K):
        res.append(dsu.size(nums[C[k]])%2)
    # print(A)
    # print(B)
    # print(C)
    # print(D)
    print(*res)
