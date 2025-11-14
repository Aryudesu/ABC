N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
data = [-1] * N
data[0] = 0
for i in range(N-1):
    if data[i] < 0:
        continue
    data[A[i]-1] = max(data[A[i]-1], data[i] + 100)
    data[B[i]-1] = max(data[B[i]-1], data[i] + 150)
print(max(data))
