N = int(input())
A = list(map(int, input().split()))
s = 0
data = []
for a in A:
    s += a
    data.append(s)
result = 0
for i in range(1, N):
    result += i*A[i] - data[i-1]
print(result)
