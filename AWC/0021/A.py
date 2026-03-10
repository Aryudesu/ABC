N, K = map(int, input().split())
result = 0
for n in range(N):
    a, *B = list(map(int, input().split()))
    result += sum(b >= K for b in B)
print(result)
