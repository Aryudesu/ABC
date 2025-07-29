N = int(input())
A = [int(l) for l in input().split()]
data = []
A.sort()
s = 0
for a in A:
    s += a
    data.append(s)
data.reverse()
A.reverse()
result = 0
for idx in range(N):
    result += A[idx] * (N - idx) - data[idx]
print(result)
