N, M = [int(l) for l in input().split()]
S = [l for l in input().split()]
T = {l for l in input().split()}
for s in S:
    print("Yes" if s in T else "No")
