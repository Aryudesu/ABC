def triNum(num, mod = 998244353):
    return ((num * (num + 1))//2) % mod

def calc(num, mod = 998244353):
    l = 1
    r = 9
    result = 0
    while r <= num:
        tmp = (triNum(r, mod) - triNum(l - 1, mod)) % mod
        tmp = (tmp * len(str(l))) % mod
        result = (result + tmp) % mod
        l = l * 10
        r = r * 10 + 9
    tmp = (triNum(num, mod) - triNum(l - 1, mod)) % mod
    tmp = (tmp * len(str(l))) % mod
    result = (result + tmp) % mod
    return result

L, R = [int(l) for l in input().split()]
mod = 10 ** 9 + 7
print((calc(R, mod) - calc(L - 1, mod)) % mod)
