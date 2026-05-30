N = int(input())
R = list(map(int, input().split()))
result = 0
for i in range(1, N - 1):
    if R[i-1] < R[i] and R[i] > R[i+1]:
        result += 1
    if R[i-1] > R[i] and R[i] < R[i+1]:
        result += 1
print(result)
