# 通ってください
N, S = [int(l) for l in input().split()]
ab = []
for n in range(N):
    ab.append([int(l) for l in input().split()])
# data[数] = [表, 裏]
data = dict()
data[0] = []
for idx in range(N):
    new_data = dict()
    a, b = ab[idx]
    for k in data:
        tmp = data.get(k, [])
        if k + a <= S:
            if not (k + a) in new_data:
                ar = [t for t in tmp]
                ar.append('H')
                new_data[k + a] = ar
        if k + b <= S:
            if not (k + b) in new_data:
                ar = [t for t in tmp]
                ar.append('T')
                new_data[k + b] = ar
    data = new_data
if S in data:
    print("Yes")
    print("".join(data[S]))
else:
    print("No")
