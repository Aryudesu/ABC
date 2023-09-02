def calc(N):
    if N % 2:
        return 0
    result = N//10
    N //= 10
    while N:
        result += N // 5
        N //= 5
    return result


print(calc(int(input())))
