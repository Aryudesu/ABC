N = int(input())
A = [int(l) for l in input().split()]
data=[]
s = 0
for idx in range(N):
    a = A[-(idx+1)]
    s += a
    data.append(s)
data.reverse()
result = 0
for idx in range(N-1):
    result += (data[idx] - data[idx+1]) * data[idx+1]
print(result)
