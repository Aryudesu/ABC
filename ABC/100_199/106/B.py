N = int(input())

result = 0
for n in range(1, N + 1):
    tmp = 0
    for k in range(1, n + 1):
        if k % 2 == 0:
            continue
        if n % k == 0:
            tmp += 1
    if tmp == 8:
        result += 1
print(result)
