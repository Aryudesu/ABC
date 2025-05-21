N = int(input())
x_data = []
y_data = []
for n in range(N):
    x, y = [int(l) for l in input().split()]
    x_data.append(x)
    y_data.append(y)
x_data.sort()
y_data.sort()
rx = x_data[N//2]
ry = y_data[N//2]
result = 0
for i in range(N):
    result += abs(rx - x_data[i])
    result += abs(ry - y_data[i])
print(result)
