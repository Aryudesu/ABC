N, Q = map(int, input().split())
S = list(map(int, input().split()))
for _ in range(Q):
    a, b = map(int, input().split())
    print("Yes" if S[a-1] > S[b-1] else "No")
