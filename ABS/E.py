N, A, B = [int(l) for l in input().split()]
result = 0
for n in range(N + 1):
    tmp = n
    num = 0
    while tmp:
        num += tmp % 10
        tmp //= 10
    if A <= num and num <= B:
        result += n
print(result)
