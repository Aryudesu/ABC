def is_prime(N):
    if N % 2 == 0:
        return False
    for n in range(3, N):
        if n * n > N:
            return True
        if N % n == 0:
            return False
    return True


print("Yes" if is_prime(int(input())) else "No")
