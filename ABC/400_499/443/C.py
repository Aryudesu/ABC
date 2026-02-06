N, T = map(int, input().split())
A = list(map(int, input().split()))
now = 0
result = 0
for n in range(N):
    if now > A[n]:
        continue
    result += A[n] - now
    now = A[n] + 100
    # print(now)
if now < T:
    result += T - now
print(result)
