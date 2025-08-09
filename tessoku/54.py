Q = int(input())
data = dict()
for _ in range(Q):
    query = input().split()
    if query[0] == "1":
        n, x, y = query
        data[x] = y
    else:
        n, x = query
        print(data[x])
