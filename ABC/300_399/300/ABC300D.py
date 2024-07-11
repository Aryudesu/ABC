def calc_primes(N):
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


def calc(N):
    PN = 1000000
    primes = calc_primes(PN)
    lp = len(primes)
    result = 0
    for idx in range(lp - 2):
        if N / (primes[idx] ** 2) < (primes[idx + 1] ** 3):
            break
        for idx2 in range(idx + 1, lp - 1):
            if N / ((primes[idx] ** 2) * primes[idx2]) < primes[idx2 + 1] ** 2:
                break
            for idx3 in range(idx2 + 1, lp):
                tmp = (primes[idx] ** 2) * primes[idx2] * (primes[idx3] ** 2)
                if tmp <= N:
                    result += 1
                else:
                    break
    return result


print(calc(int(input())))
