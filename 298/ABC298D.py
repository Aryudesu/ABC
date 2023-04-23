Q = int(input())
MOD = 998244353
num = 1
result = []
data = [1]
idx = 0
for q in range(Q):
    query = [int(l) for l in input().split()]
    if query[0] == 1:
        num = (num * 10 + query[1]) % MOD
        data.append(query[1])
    elif query[0] == 2:
        tmp = (data[idx] * pow(10, len(data) - idx - 1, MOD)) % MOD
        num = (num - tmp) % MOD
        idx += 1
    elif query[0] == 3:
        result.append(num)
for r in result:
    print(r)
