N, P, T, C = map(int, input().split())
if N > 1:
    S = list(map(int, input().split()))
else:
    S = []
if P >= T:
    print(0)
else:
    if S:
        m = max(S)
    else:
        m = -1
    if m >= T:
        print(C)
    else:
        print(-1)
