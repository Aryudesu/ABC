mod = 998244353
# 絶対TLEする・・・・・・orz
N, A1, A2, A3 = [int(l) for l in input().split()]
result = 0
X1 = A1
while X1 <= N:
    X2 = A2
    while X2 <= N:
        X3 = X1 ^ X2
        if X3 and X3 <= N and X3 % A3 == 0:
            result = (result + 1) % mod
        X2 += A2
    X1 += A1
print(result)
