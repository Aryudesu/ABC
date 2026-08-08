def calcDiv(num: int)->list[int]:
    result = []
    for i in range(1, num+1):
        if num % i == 0:
            result.append(i)
    return result

def str2bit(S: str)->int:
    result = 0
    for s in S:
        result <<= 1
        if s == "A":
            result |= 1
    return result

def shiftL(num: int, L: int)->int:
    l = (num << 1) & MASK
    r = (num >> (L - 1)) & MASK
    return l + r

def shiftR(num: int, L: int)->int:
    l = (num >> 1) & MASK
    r = ((num & 1) << (L - 1)) & MASK
    return l + r

def getRepeat(num: int, L: int, divs: list[int])->list[int]:
    result = []
    for d in divs:
        res = 0
        base = num >> (L - d)
        for _ in range(L // d):
            res <<= d
            res |= base
        result.append(res)
    return result

N = int(input())
MASK = (1 << N) - 1
S = input()
T = input()
nodes = set()
nodes.add(str2bit(S))
goal = str2bit(T)
memo = set()
divs = calcDiv(N)
result = 0
isOk = False
if goal in nodes:
    print(0)
    exit(0)
while nodes:
    result += 1
    nextNodes = set()
    for node in nodes:
        nextN = shiftL(node, N)
        if nextN not in memo:
            nextNodes.add(nextN)
            memo.add(nextN)
        nextN = shiftR(node, N)
        if nextN not in memo:
            nextNodes.add(nextN)
            memo.add(nextN)
        nexts = getRepeat(node, N, divs)
        for nextN in nexts:
            if nextN not in memo:
                nextNodes.add(nextN)
                memo.add(nextN)
    if goal in nextNodes:
        isOk = True
        break
    nodes = nextNodes
    # print(nodes, goal)
if isOk:
    print(result)
else:
    print(-1)
