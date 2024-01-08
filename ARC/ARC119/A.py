N = int(input())
if N <= 1:
    print(N)
else:
    b = 0
    m = 1
    result = (10**10, 10**10, 10**10)
    while m <= N:
        a = N // m
        c = N - a * m
        if sum(result) >= max((a, b, c)):
            result = (a, b, c)
        m <<= 1
        b += 1
    print(sum(result))
