N = int(input())
A = list(map(int, input().split()))
S = sum(A)
B = [abs(N * a - S) for a in A]
m = max(B)
print(B.index(m) + 1)
