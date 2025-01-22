def calc(N):
    tmp = 1
    count = 0
    while tmp < N:
        count += 1
        tmp *= count
    return count

print(calc(int(input())))
