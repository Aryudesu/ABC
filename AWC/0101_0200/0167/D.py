N, K = map(int, input().split())
A = list(map(int, input().split()))
if N == 1:
    print(1)
    exit(0)
route = [0]
memo = {0}
loop = False
pos = 0
for k in range(K):
    if pos == N-1:
        print(N)
        exit(0)
    else:
        if (A[pos] + A[pos+1]) % 2:
            pos = max(0, pos - 1)
        else:
            pos = pos + 1
    if pos in memo:
        loop = True
        route.append(pos)
        break
    route.append(pos)
    memo.add(pos)
if len(route) == K + 1:
    print(route[-1] + 1)
    exit(0)
elif len(route) == 2 and route[0] == route[1] == 0:
    print(1)
    exit(0)
elif route[-1] == N - 1:
    print(N)
    exit(0)
D = K - route[-1]
if D % 2:
    print(route[-1] + 2)
else:
    print(route[-1] + 1)
