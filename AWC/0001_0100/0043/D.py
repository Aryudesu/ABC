N = int(input())
A = list(map(int, input().split()))
A.sort()
data = []
s = 0
for i in range(N):
    s += A[i]
    data.append(s)
# 1  2 3 4
# 1  3 6 10
# 3 + 6 + 10 - 1 * 3
# (3 - 1) + 6 + 10 - 3 * 2

result = 0
for i in range(N):
    result += data[-1] - data[i]
    result -= A[i] * (N-i-1)
# print(data)
print(result)
