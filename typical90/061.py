Q = int(input())
upper = []
lower = []
count = 0
result = []
for _ in range(Q):
    t, x = [int(l) for l in input().split()]
    if t == 1:
        upper.append(x)
    elif t == 2:
        lower.append(x)
    elif t == 3:
        lsize = len(lower)
        usize = len(upper)
        if x <= usize:
            result.append(upper[-x])
        else:
            idx = x - usize - 1
            result.append(lower[idx])

for r in result:
    print(r)
