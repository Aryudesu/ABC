mod = 998244353


def calc_inv(num):
    return pow(num, mod - 2, mod)


def calc_div(numer, denoms):
    n = numer
    d = 1
    for denom in denoms:
        d = (d * calc_inv(denom)) % mod
    return (n * d) % mod


N = int(input())
A = [int(l) for l in input().split()]
data = [0] * 11
data[0] = 1
for a in A:
    new_data = [0] * 11
    num = a if a < 10 else 10
    for n in range(num + 1):
        for m in range(11):
            if n + m <= 10:
                new_data[n + m] += data[m] + data[n] * (a-n)
    data = new_data
    print(data)
print(calc_div(data[10], A))
