N = int(input())
a, b = 1, 1
MOD = 10 ** 9
memo = set()
for n in range(N-2):
    tmp = (a, b)
    if tmp in memo:
        break
    memo.add(tmp)
    a, b = b, (a + b) % MOD
print(b)
