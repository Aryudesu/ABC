N = int(input())
A = []
for n in range(N):
    l, *a = list(map(int, input().split()))
    A.append(a)
X, Y = map(int, input().split())
print(A[X-1][Y-1])
