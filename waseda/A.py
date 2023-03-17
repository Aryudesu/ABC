N, M = [int(l) for l in input().split()]
print(sum([(l+1)**2 for l in range(N)]) % M)
