result = []
for i in range(2, 2025):
    j = 2
    while True:
        tmp = pow(i, j)
        if 2025 <= tmp <= 2125:
            result.append([tmp, i, j])
        elif tmp > 2025:
            if tmp < 3000:
                result.append([tmp, i, j])
            break
        j += 1
result.sort()
for i, j, k in result:
    print(i, j, k)
