# 4平方和定理
def calc(data: list)-> int:
    if not data:
        return 1
    MOD = 998244353
    data_dict = dict()
    for n in data:
        if n == 2 and n in data_dict:
            continue
        data_dict[n] = (data_dict.get(n, 1) * n + 1)%MOD
    result = 8
    for k in data_dict:
        result = (result * data_dict.get(k, 1)) % MOD
    return result

_ = int(input())
nums = [int(l) for l in input().split()]
result1 = calc(nums)
print(result1)
