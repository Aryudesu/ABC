from itertools import combinations
from bisect import bisect_right

def makeData(nums: list[int], num: int)-> list[int]:
    if num == 0:
        return [0]
    result = list()
    for dat in combinations(nums, num):
        result.append(sum(dat))
    result.sort()
    return result

N, K, P = map(int, input().split())
A = list(map(int, input().split()))
A1 = []
A2 = []
l = N // 2
for i in range(N):
    a = A[i]
    if i < l:
        A1.append(a)
    else:
        A2.append(a)

result = 0
for i in range(K + 1):
    if K - i < 0:
        break
    data1 = makeData(A1, i)
    data2 = makeData(A2, K - i)
    for d1 in data1:
        result += bisect_right(data2, P - d1)
print(result)
