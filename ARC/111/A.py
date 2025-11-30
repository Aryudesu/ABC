N, M = map(int, input().split())
tmp = pow(10, N, M ** 3)
print((tmp//M) % M)
