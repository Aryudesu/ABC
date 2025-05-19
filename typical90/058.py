def calc10(num):
    result = 0
    tmp = num
    while tmp != 0:
        result += tmp % 10
        tmp = tmp // 10
    return result


def calc(N, K, MOD=10**5):
    num = N
    count = 0
    data = {num: 0}
    while count < K:
        num = (num + calc10(num)) % MOD
        if data.get(num) is not None:
            break
        count += 1
        data[num] = count
    loop_num = (count - data[num] + 1) % K
    if loop_num == 0:
        return num
    M = (K - data[num]) % loop_num
    for m in range(M):
        num = (num + calc10(num)) % MOD
    return num


dataSet = dict()
N, K = [int(l) for l in input().split()]
print(calc(N, K))
