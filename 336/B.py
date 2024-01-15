def ctz(N):
    result = 0
    tmpN = N
    while True:
        if tmpN % 2:
            break
        result += 1
        tmpN >>= 1
    return result

N = int(input())
print(ctz(N))
