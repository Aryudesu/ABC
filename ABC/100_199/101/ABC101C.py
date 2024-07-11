N, K = [int(l) for l in input().split()]
A = [int(l) for l in input().split()]
tmp1 = (N - 1)//(K-1)
tmp2 = 1 if (N - 1) % (K-1) else 0
print(tmp1 + tmp2)
