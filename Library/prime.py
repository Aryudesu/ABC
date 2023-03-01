import time


def calc_time(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        print(func.__name__, time.time() - start)
        return result
    return wrapper


def is_prime(num, primes):
    for prime in primes:
        if not num % prime:
            return False
        if prime**2 > num:
            return True
    return True


@calc_time
def calc_prime(num):
    if num < 2:
        return []
    primes = [2]
    for i in range(3, num, 2):
        if is_prime(i, primes):
            primes.append(i)
    return primes


N = 1000000
result = calc_prime(N)
