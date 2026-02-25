N, T = map(int, input().split())
H = list(map(int, input().split()))
C = list(map(int, input().split()))
result = 0
for i in range(N):
    if H[i] <= T:
        result += C[i]
print(result)
