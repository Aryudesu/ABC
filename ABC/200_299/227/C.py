N = int(input())
result = 0
for a in range(1, N + 1):
    if a ** 3 > N:
        break
    for b in range(a, N + 1):
        if a * b * b > N:
            break
        tmp = N // (a * b)
        result += tmp - b + 1
print(result)
