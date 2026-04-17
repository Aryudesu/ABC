N = int(input())
H = list(map(int, input().split()))
D = list(map(int, input().split()))
data = [0] * N
if H[0] and D[0]:
    data[0] = 1
data[1] = data[0]
if H[1] and D[1]:
    data[1] += 1

for i in range(2, N):
    data[i] = min(data[i-1], data[i-2])
    if H[i] and D[i]:
        data[i] += 1
# print(data)
print(data[-1])
