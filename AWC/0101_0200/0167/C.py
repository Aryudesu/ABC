N, M, K = map(int, input().split())
D = list(map(int, input().split()))
if N == 1:
    print(0)
    exit(0)
dist = 0
count = 1
for d in D:
    dist += d
    if dist >= K:
        count += 1
        dist = 0
if dist >= K:
    count += 1
print(sum(D) if count >= N else -1)
