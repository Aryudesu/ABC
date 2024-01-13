N = int(input())
A = [int(l) for l in input().split()]
# [日][0:やらない / 1:やる]
data = [[0, 0] for l in range(N + 1)]
for n in range(N):
    data[n + 1][0] = max([data[n][0], data[n][1]])
    if n - 1 >= 0:
        data[n + 1][0] = max([data[n + 1][0], data[n - 1][0], data[n - 1][1]])
    data[n + 1][1] = data[n][0] + A[n]
    if n - 1 >= 0:
        data[n + 1][1] = max([data[n + 1][1], data[n - 1][0] + A[n], data[n - 1][1] + A[n]])
print(max(data[-1]))
