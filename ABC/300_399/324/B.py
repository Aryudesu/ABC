def calc(N):
    tmp = N
    while tmp % 2 == 0:
        tmp >>= 1
    while tmp % 3 == 0:
        tmp //= 3
    return tmp == 1


N = int(input())
print("Yes" if calc(N) else "No")
