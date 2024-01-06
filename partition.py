def partition(num, mem):
    result = 0
    for i in range(1, num + 1):
        gokaku = [i * (3 * i - 1) // 2, i * (3 * i + 1) // 2]
        if num < gokaku[0] and num < gokaku[1]:
            break
        for g in gokaku:
            if num >= g:
                if i % 2:
                    result += mem[num - g]
                else:
                    result -= mem[num - g]
    return result


def calcPartition(num):
    result = [1]
    for i in range(1, num + 1):
        result.append(partition(i, result))
    return result

num = int(input())
print(calcPartition(num)[-1])