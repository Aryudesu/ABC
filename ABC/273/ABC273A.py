def calc(N):
    if not N:
        return 1
    return N * calc(N - 1)


print(calc(int(input())))
