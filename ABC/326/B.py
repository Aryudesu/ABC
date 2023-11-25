def calc(N):
    tmp = N
    while True:
        if (tmp // 100) * ((tmp//10) % 10) == tmp % 10:
            return tmp
        tmp += 1


N = int(input())
print(calc(N))
