N = int(input())
MOD = 10000
result = []
res = 0
for n in range(N):
    T, A = [l for l in input().split()]
    A = int(A)
    if T == "+":
        res = (res + A) % MOD
    elif T == "-":
        res = (res - A) % MOD
    elif T == "*":
        res = (res * A) % MOD
    else:
        raise Exception()
    result.append(res)

for r in result:
    print(r)
