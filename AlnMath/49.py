N = int(input())
a, b = 1, 1
MOD = 10 ** 9 + 7
for n in range(N-2):
    a, b = b, (a + b) % MOD
print(b)
