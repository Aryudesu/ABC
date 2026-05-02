N, K = map(int, input().split())
A = list(map(int, input().split()))
A.sort(reverse=True)
print(sum(a//2 for a in A[:K]) + sum(A[K:]))
