def calc10(num):
    result = 0
    tmp = num
    while tmp != 0:
        result += tmp % 10
        tmp = tmp // 10
    return result


data = []
dataSet = set()
N, K = [int(l) for l in input().split()]
MOD = 10**5
num = N
count = 0
while count < K:
    next = (num + calc10(num)) % MOD
    if next in dataSet:
        break
    data.append(next)
    dataSet.add(next)
    count += 1
    num = next
if count == K:
    print(data[-1])
else:
    base = data.index(next)
    print(data[(K - base) % (count - base) + base - 1])
