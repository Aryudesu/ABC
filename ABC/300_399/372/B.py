def calc(M):
    result = []
    tmp = M
    count = 0
    while tmp > 0:
        num = tmp % 3
        tmp //= 3
        for n in range(num):
            result.append(count)
        count += 1
    return result


M = int(input())
result = calc(M)
print(len(result))
print(*result)
