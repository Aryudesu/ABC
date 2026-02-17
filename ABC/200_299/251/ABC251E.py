INF = 10 ** 18
N = int(input())
A = list(map(int, input().split()))
data = []
for n in range(N):
    data.append([INF, INF, INF, INF])
data[0][0] = A[0]
data[0][3] = 0
for i in range(1, N):
    data[i][0] = min(data[i-1][0] + A[i], data[i-1][1] + A[i], data[i][0])
    data[i][1] = min(data[i-1][0], data[i][1])
    data[i][2] = min(data[i-1][2] + A[i], data[i-1][3] + A[i], data[i][2])
    data[i][3] = min(data[i-1][2], data[i][3])
print(min(data[-1][0], data[-1][1], data[-1][2]))
