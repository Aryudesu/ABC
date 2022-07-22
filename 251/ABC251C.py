N = int(input())
res = dict()
max = 0
maxidx = 0
for idx in range(N):
    A, B = input().split()
    S = A
    T = int(B)
    if res.get(S):
        continue
    if max < T:
        max = T
        maxidx = idx + 1
    res[S] = T
print(maxidx)
