N, M = [int(l) for l in input().split()]
A = [int(l) for l in input().split()]
data = {i for i in range(1, M + 1)}
counter = dict()
f = True
for a in A:
    counter[a] = counter.get(a, 0) + 1
    if 1 <= a <= M:
        f = False
    data.discard(a)
if data:
    print(0)
else:
    for i in range(N):
        a = A[-(i + 1)]
        if 1 <= a <= M:
            counter[a] -= 1
            if counter[a] == 0:
                print(i + 1)
                break
