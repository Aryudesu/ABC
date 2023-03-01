def calc(N):
    data = N
    result = []
    while data % 2 == 0:
        result.append(2)
        data //= 2
    for n in range(3, N, 2):
        while data % n == 0:
            result.append(n)
            data //= n
        if data == 1:
            break
    return result


result = calc(int(input()))
print(*result)
