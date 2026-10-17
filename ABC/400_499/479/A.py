N = int(input())
A = list(map(int, input().split()))
print(sum(A[idx] for idx in range(0, N, 2)))
