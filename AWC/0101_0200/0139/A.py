N = int(input())
A = list(map(int, input().split()))
data = [0] * (N + 1)
for a in A:
    data[a] += 1
result = 0
for idx in range(N + 1):
    if data[idx] > data[0]:
        result += 1
print(result)
