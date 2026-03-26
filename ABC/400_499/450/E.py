from collections import defaultdict

def makeFibs(X: str, Y: str)->list[int]:
    fibs = [len(X), len(Y)]
    x1 = len(Y)
    x2 = len(X)
    M = 10 ** 18
    while x1 <= M and x2 <= M:
        x1, x2 = x1 + x2, x1
        fibs.append(x1)
    return fibs

def makeCData(X: str, Y: str, lenFib: int):
    xCount = defaultdict(int)
    yCount = defaultdict(int)
    for x in X:
        xCount[x] += 1
    for y in Y:
        yCount[y] += 1
    keys = set(xCount.keys())
    keys.update(set(yCount.keys()))
    data = defaultdict(list)
    for c in keys:
        res = [xCount[c], yCount[c]]
        while len(res) < lenFib:
            res.append(res[-1] + res[-2])
        data[c] = res
    return data

def prod(n: int, fibs: list[int], data: list[int])->int:
    N = len(fibs)
    result = 0
    idx = N-1
    num = n
    while idx > 1:
        if fibs[idx-2] < num:
            num = num - fibs[idx-2]
            result += data[idx-2]
            idx -= 1
        else:
            idx -= 2
    if idx == 1 and num > fibs[0]:
        result += data[0]
    return result
            


def calc(l: int, r: int, fibs: list[int], cData: list[int])-> int:
    return prod(r+1, fibs, cData) - prod(l, fibs, cData)


X = input()
Y = input()
Q = int(input())
fibs = makeFibs(X, Y)
cData = makeCData(X, Y, len(fibs))
result = []
for _ in range(Q):
    l, r, c = input().split()
    l, r = int(l), int(r)
    if len(cData[c]) == 0:
        result.append(0)
        continue
    result.append(calc(l, r, fibs, cData[c]))
for r in result:
    print(r)
