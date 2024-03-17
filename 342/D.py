def calc_prime(N):
    """素数表作成"""
    result = [True] * (N + 1)
    primes = [2]
    for i in range(3, N + 1, 2):
        if not result[i]:
            continue
        primes.append(i)
        idx = 3
        while idx * i <= N:
            result[idx * i] = False
            idx += 2
    return primes

def calc_dis_square_factor(num, primes):
    """平方因子でないものの抽出"""
    if num == 0:
        return 0
    if num == 1:
        return 1
    tmp = num
    result = 1
    for p in primes:
        if tmp < p:
            break
        count = 0
        while tmp % p == 0:
            tmp //= p
            count += 1
        if count % 2:
            result *= p
    result *= tmp
    return result

primes = calc_prime(600)
N = int(input())
A = [int(l) for l in input().split()]
data = dict()
for a in A:
    tmp = calc_dis_square_factor(a, primes)
    data[tmp] = data.get(tmp, 0) + 1
result = 0
for k in data:
    tmp = data.get(k, 0)
    if k == 0:
        result += tmp * (N - tmp)
    result += (tmp * (tmp - 1)) // 2
print(result)
