def calc10(num):
    result = 0
    tmp = num
    while tmp != 0:
        result += tmp % 10
        tmp = tmp // 10
    return result


dataSet = dict()
N, K = [int(l) for l in input().split()]
MOD = 10**5
num = N
count = 0
while count < K:
    if num in dataSet:
        break
    dataSet[num] = count
    num = (num + calc10(num)) % MOD
    count += 1
result = 0
if count == K:
    result = num
else:
    print(count)
    print(num)
