import time


def calc_time(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        print(func.__name__, time.time() - start)
        return result
    return wrapper


@calc_time
def calc_primes(N):
    is_prime = [True] * (N + 1)
    is_prime[0] = is_prime[1] = False
    for i in range(2, int(N**0.5) + 1):
        if is_prime[i]:
            for j in range(i*i, N+1, i):
                is_prime[j] = False
    primes = []
    for i in range(2, N+1):
        if is_prime[i]:
            primes.append(i)
    return primes


N = 1000
result = calc_primes(N)
print(*result)
