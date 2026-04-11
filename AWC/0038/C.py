N, L, K = map(int, input().split())
A = list(map(int, input().split()))
A.sort()
s = 0
count = 0
for a in A:
    s += a
    if s > L:
        break
    count += 1
    if count >= K+1:
        break
print(count)
