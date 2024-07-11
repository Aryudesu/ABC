N, S, K = [int(l) for l in input().split()]
s = 0
for n in range(N):
    p, q = [int(l) for l in input().split()]
    s += p * q
if s < S:
    s += K
print(s)
