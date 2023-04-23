def calc(B, C):
    MOD = 10 ** 9 + 7
    idx = 10 % B
    num = B
    data = {c: 1 for c in C}
    result = {0: 0}
    while num:
        new_data = dict()
        for n in data:
            for m in data:
                tmp = (idx * n + m) % B
                d = (data.get(n) + data.get(m) + new_data.get(tmp, 0)) % MOD
                new_data[tmp] = d

        if num % 2:
            tmp_result = dict()
            for r in result:
                for d in data:
                    tmp = (r + d) % B
                    n = result.get(r, 0) + data.get(d, 0)
                    n += tmp_result.get(tmp, 0)
                    tmp_result[tmp] = n
            result = tmp_result

        num >>= 1
        idx = (idx * idx) % MOD
        data = new_data
        print(result)
    return result.get(0, 0)


N, B, K = [int(l) for l in input().split()]
C = [int(l) for l in input().split()]
print(calc(B, C))
