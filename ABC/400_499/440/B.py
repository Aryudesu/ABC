N = int(input())
T = list(map(int, input().split()))
data = []
for i in range(N):
    data.append((T[i], i + 1))
data.sort()
result = [data[0][1], data[1][1], data[2][1]]
print(*result)
