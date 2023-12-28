N = int(input())
data = [0] * (N + 1)
data[0] = 1
for n in range(N):
    i = n
    j = n + 1
    if j < N + 1:
        data[j] += data[i]
    j = n + 2
    if j < N + 1:
        data[j] += data[i]
print(data[-1])
