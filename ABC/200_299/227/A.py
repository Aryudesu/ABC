N, K, A = [int(l) for l in input().split()]
tmp = (A + K - 1) % N
print(tmp if tmp else N)
