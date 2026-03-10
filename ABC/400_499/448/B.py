N, M = map(int, input().split())
C = list(map(int, input().split()))
result = 0
for n in range(N):
    a, b = map(int, input().split())
    c = C[a-1]
    if C[a-1] > b:
        result += b
        C[a-1] -= b
    else:
        result += C[a-1]
        C[a-1] = 0
print(result)
