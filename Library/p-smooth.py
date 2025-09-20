import heapq

def make_p_smooth(limit: int, primes: list[int], visit):
    if limit < 1:
        return
    primes = sorted(set(primes))
    stack = [(1, 0)]
    while stack:
        cur, i = stack.pop()
        visit(cur)  # 1 も含む
        for j in range(i, len(primes)):
            p = primes[j]
            v = cur
            while True:
                v *= p
                if v > limit:
                    break
                stack.append((v, j + 1))


def checkData(num: int, target: int) -> bool:
    result = 1
    while num:
        result *= num % 10
        num //= 10
    return result == target

def calc(N, B):
    limit = min(9 ** 11, N - B)
    if N < B:
        return 0
    result = 0    
    if checkData(B, 0):
        result += 1
    for p in makePSmooth(limit, [2, 3, 5, 7]):
        if B + p <= N and checkData(B + p, p):
            result += 1
    return result

N, B = [int(l) for l in input().split()]
print(calc(N, B))
