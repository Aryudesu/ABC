MOD = 998244353
S = input()
a = 0
b = 0
c = 0
for s in S:
    if s == "a":
        a = (a + 1 + b + c) % MOD
    elif s == "b":
        b = (b + 1 + a + c) % MOD
    elif s == "c":
        c = (c + 1 + a + b) % MOD
print((a + b + c) % MOD)
