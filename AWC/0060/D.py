from itertools import product

N = int(input())
PQ = []
for n in range(N):
    p, q = map(int, input().split())
    PQ.append((p, q))
MAX = N * N
result = MAX
for dat in product([0, 1], repeat=N):
    s = sum(dat)
    if s < 2:
        continue
    omote = 1
    ura = 1
    for n in range(N):
        if dat[n] == 1:
            omote *= PQ[n][0]
            ura *= PQ[n][1]
    if omote == ura:
        result = min(result, sum(dat))
print(result if result < MAX else -1)
