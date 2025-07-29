MOD = 998244353

def calc(num: int) -> int:
    return ((num * (num + 1))//2) % MOD


A, B, C = [int(l) for l in input().split()]
print((((calc(A) * calc(B)) % MOD) * calc(C)) % MOD)
