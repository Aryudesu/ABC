N = int(input())
A = list(map(int, input().split()))
A.sort()
count = 0
for i in range(N-1):
    if A[i] + 1 != A[i+1]:
        count += 1
print(count+1)
