N = int(input())
P = list(map(int, input().split()))
A = list(map(int, input().split()))
B = list(map(int, input().split()))
result = sum(A) - sum(B)
M = 0
for p, a, b in zip(P, A, B):
    M = max(M, (p - b) - (a - b))
print(result + M)
