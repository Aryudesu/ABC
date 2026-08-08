def calcDivisors(num: int)->list[int]:
    result = []
    primes = [2, 3, 5, 7]
    for p in primes:
        while num % p == 0:
            result.append(p)
            num //= p
    if num > 1:
        result.append(num)
    return result

def calc(N: int, M: int)->int:
    # 約数列挙
    divisors = calcDivisors(M)
    # 素因数分解で2桁以上の素数があれば無理
    if not divisors:
        return 1
    if divisors[-1] > 9:
        return 0
    [0] * 10
    for i in range(len(str(N))):
        pass
    return 0

N, M = map(int, input().split())
print(calc(N, M))
