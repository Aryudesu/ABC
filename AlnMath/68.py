from math import gcd

def lcm(V: list[int], threshold: int=10 ** 18)->int|None:
    result = 1
    for v in V:
        result = result * v // gcd(result, v)
        if result > threshold:
            return result
    return result


def calcMultipleNums(N: int, V: list[int])->int:
    result = 0
    K = len(V)
    for num in range(1, 1 << K):
        mask = num
        tmp = []
        for i in range(K):
            if mask & 1:
                tmp.append(V[i])
            mask >>= 1
        if len(tmp) % 2:
            result += N // lcm(tmp, N)
        else:
            result -= N // lcm(tmp, N)
    return result
            
N, K = map(int, input().split())
V = list(set(map(int, input().split())))
print(calcMultipleNums(N, V))
