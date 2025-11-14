N = int(input())
field = []
for i in range(N):
    field.append(list(map(int, input().split())))
result = []
Q = int(input())
col = list(range(N))
for _ in range(Q):
    n, x, y = map(int, input().split())
    x, y = x - 1, y - 1
    if n == 1:
        col[x], col[y] = col[y], col[x]
    else:
        tx, ty = col[x], y
        result.append(field[tx][ty])
    # for n in range(N):
    #     print(field[col[n]])
for r in result:
    print(r)
