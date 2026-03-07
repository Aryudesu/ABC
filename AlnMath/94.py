N = int(input())
B = list(map(int, input().split()))
data = [(B[0], B[0])]
for i in range(N-2):
    b1, b2 = min(B[i], B[i+1]), max(B[i], B[i+1])
    data.append((b1, b2))
data.append((B[-1], B[-1]))
result = 0
for m, M in data:
    result += m
print(result)
