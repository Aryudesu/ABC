N, L, R, M = map(int, input().split())
result = 0
for n in range(N):
    p, k = map(int, input().split())
    if not (L <= p <= R):
        continue
    if M < k:
        continue
    result += 1
print(result)
