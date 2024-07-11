N = int(input())
res = 0
for n in range(1, N):
    p, m = divmod(N, n)
    res += p - (0 if m else 1)
print(res)
