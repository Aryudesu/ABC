N = int(input())
data = {n for n in range(N + 1)}
L = [int(l) for l in input().split()]
data.discard(0)
data.discard(N)
for n in range(N):
    if L[n] == 1:
        break
    data.discard(n + 1)
for n in range(N):
    if L[-n-1] == 1:
        break
    data.discard(N - n - 1)
print(len(data))
