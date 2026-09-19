N, D, S = map(int, input().split())
A = list(map(int, input().split()))
SA = sum(A)
result = (D // N) * SA
for d in range(D % N):
    result += A[(S - 1 + d) % N]
print(result)
