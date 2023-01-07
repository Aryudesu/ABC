import math


def is_prime(num, primes):
    for prime in primes:
        if not num % prime:
            return False
        if prime**2 > num:
            return True
    return True


def calc_prime(num):
    if num < 2:
        return []
    primes = [2]
    for i in range(3, num, 2):
        if is_prime(i, primes):
            primes.append(i)
    t_num = len(primes)
    approx = num/math.log(num)
    print(t_num)
    print(approx)
    print(100*(t_num - approx)/t_num, "%")
    return primes


def input_num():
    while True:
        try:
            print("Input Number > ", end='')
            return int(input())
        except:
            pass


result = calc_prime(input_num())
# print(*result)
