N = int(input())
data = [0] * N
for n in range(N-1):
    a, b = [int(l) - 1 for l in input().split()]
    data[a] += 1
    data[b] += 1
data.sort()
print("Yes" if data[-1] == N - 1 and data[-2] == 1 else "No")
