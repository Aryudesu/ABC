from math import gcd

def calcDiv(H: int, W: int, S: int)->set[int]:
    result = set()
    G = gcd(H, W)
    for i in range(1, G+1):
        if i * i > G:
            break
        if G % i:
            continue
        tmp = (H // i) * (W // i)
        if tmp % S == 0:
            result.add(i)
        tmp = (H // (G//i)) * (W // (G//i))
        if tmp % S == 0:
            result.add(G//i)
    return result

def updateDiv(H: int, W: int, S: int, memo: set[int])->set[int]:
    result = set()
    G = gcd(H, W)
    for num in memo:
        if G % num:
            continue
        tmp = (H // num) * (W // num)
        if tmp % S == 0:
            result.add(num)
    return result

N = int(input())
h, w, s = map(int, input().split())
cache = set()
cache.add((max(h, w), min(h, w), s))
memo = calcDiv(h, w, s)
for n in range(N-1):
    h, w, s = map(int, input().split())
    if (max(h, w), min(h, w), s) in cache:
        continue
    cache.add((max(h, w), min(h, w), s))
    memo = updateDiv(h, w, s, memo)
print(max(memo))
