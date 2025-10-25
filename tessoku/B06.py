N = int(input())
A = [int(l) * 2 - 1 for l in input().split()]
data = [0]
s = 0
for a in A:
    s += a
    data.append(s)

result = []
Q = int(input())
for q in range(Q):
    L, R = [int(l) for l in input().split()]
    tmp = data[R] - data[L-1]
    if tmp == 0:
        result.append("draw")
    elif tmp > 0:
        result.append("win")
    else:
        result.append("lose")
for r in result:
    print(r)
