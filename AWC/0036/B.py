data = set()
result = []
Q = int(input())
for _ in range(Q):
    t, x = map(int, input().split())
    if t == 1:
        data.add(x)
    elif t == 2:
        if x in data:
            result.append("Yes")
        else:
            result.append("No")
    else:
        raise ValueError()
for r in result:
    print(r)
