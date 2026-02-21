K, M = map(int, input().split())
L = list(map(int, input().split()))
result = sum(L) % M
print(result)
