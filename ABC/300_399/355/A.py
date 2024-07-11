A, B = [int(l) for l in input().split()]
data = set([1, 2, 3])
data.discard(A)
data.discard(B)
if len(data) == 1:
    print(data.pop())
else:
    print(-1)
