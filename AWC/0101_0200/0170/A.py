N = int(input())
result = 0
score = -10000
data = []
data.append(-10000)
for n in range(N):
    h, s, d = map(int, input().split())
    data.append(h + s)
    if data[-1] > data[result]:
        result = n + 1
print(result)
