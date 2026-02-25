N, K, M = map(int, input().split())
HP0 = []
HP1 = []
for n in range(N):
    h, p = map(int, input().split())
    if h == 1:
        HP1.append(p)
    elif h == 0:
        HP0.append(p)
    else:
        raise ValueError()
HP0.sort(reverse=True)
HP1.sort(reverse=True)
if len(HP1) >= M and len(HP0) >= K-M:
    print(sum(HP1[:M]) + sum(HP0[:K-M]))
else:
    print(-1)
