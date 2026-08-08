N, M = map(int, input().split())
A = list(map(int, input().split()))
for a in A:
    q, r = divmod(a, M)
    print(q, r)
