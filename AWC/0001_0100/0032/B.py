N, K, M = map(int, input().split())
A = list(map(int, input().split()))
result = 0
KX = K + M
for a in A:
    result += (a + KX - 1) // KX
print(result)
