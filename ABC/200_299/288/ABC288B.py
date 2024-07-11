N, K = [int(l) for l in input().split()]
S = []
for n in range(N):
    if n >= K:
        input()
    else:
        S.append(input())
S.sort()
for s in S:
    print(s)
