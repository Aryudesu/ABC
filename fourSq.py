# 4平方和定理

def input_data(N: int)-> list:
    return [int(input()) for _ in range(N)]

def calc(data: list)-> int:
    MOD = 998244353
    data_dict = dict()

    for n in data:
        if n == 2 and n in data_dict:
            continue
        data_dict[n] = (data_dict.get(n, 1) * n + 1) % MOD

    result = 1

    for k in data_dict:
        result *= data_dict.get(k, 1)

    return result * 8

nums = input_data(int(input()))
result1 = calc(nums)
print(result1)
