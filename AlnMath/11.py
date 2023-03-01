def is_prime(N, prime):
    for p in prime:
        if p*p > N:
            return True
        if N % p == 0:
            return False
    return True


N = int(input())
prime = [2]
for n in range(3, N + 1):
    if is_prime(n, prime):
        prime.append(n)
print(*prime)
