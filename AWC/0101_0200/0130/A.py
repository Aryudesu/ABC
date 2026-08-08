N, M = map(int, input().split())
S = input()
data = [1 if s == "A" else -1 for s in S]
K = sum(data)
for m in range(M):
    R = int(input()) - 1
    if data[R] == 1:
        K -= 2
    else:
        K += 2
    data[R] *= -1
    if abs(K) == N:
        print(m + 1)
        exit(0)
print(-1)
