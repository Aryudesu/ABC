N, M, S = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
D = sum(A) - sum(B)
if D >= 0:
    print(-1)
else:
    print(S//(-D))
