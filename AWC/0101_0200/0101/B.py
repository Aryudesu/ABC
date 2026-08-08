N = int(input())
A = list(map(int, input().split()))
M = max(A)
print(M if A[0] == M else M - 1)
