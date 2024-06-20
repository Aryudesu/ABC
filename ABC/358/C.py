def int2Bit(num, N):
    result = []
    tmp = num
    for _ in range(N):
        result.append(tmp % 2)
        tmp //= 2
    return result

N, M = [int(l) for l in input().split()]
goal = (1 << M) - 1
# print(goal)
data = []
for n in range(N):
    S = input()
    tmp = 0
    for s in S:
        tmp <<= 1
        if s == "o":
            tmp |= 1
    data.append(tmp)
# print(data)
result = 10 * N
for n in range(2 ** N):
    ibData = int2Bit(n, N)
    count = 0
    tmp = 0
    for n in range(N):
        if ibData[n]:
            count += 1
            tmp |= data[n]
    if tmp == goal:
        if result > count:
            result = count
print(result)
