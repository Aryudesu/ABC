from collections import defaultdict
from sortedcontainers import SortedList

N, K = map(int, input().split())
BA = []
AB = SortedList()
A = []
for n in range(N):
    a, b = map(int, input().split())
    BA.append((b, a))
    AB.add((a, b))
    A.append(a)
A.sort(reverse=True)
BA.sort()
# 一旦上位K個の総和
KSum = 0
for k in range(K-1):
    KSum += A[k]
# print(KSum)
result = 0
for b, a in BA:
    if len(AB) < K:
        break
    bTmp = b
    leq = AB.bisect_right((a, b))
    if len(AB) - leq + 1 <= K-1:
        KSum -= a
        AB.discard((a, b))
        # print("len(AB)-K+1", len(AB)-K+1)
        KSum += AB[len(AB)-K+1][0]
        res = (a + KSum) * b
        result = max(result, res)
    else:
        AB.discard((a, b))
        res = (a + KSum) * b
        result = max(result, res)
print(result)
