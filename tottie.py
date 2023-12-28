N = 2022
result = []
count = 0
while count < 10000000:
    tmp = N + count ** 2
    tmp2 = int(tmp ** 0.5)
    for i in range(3):
        if (tmp2 + (i-1))** 2 - count ** 2 == N:
            result.append((tmp2 + (i-1), count))
    count += 1
print(result)