N, M = map(int, input().split())
data = set()
result = []
for n in range(N):
    L = int(input())
    X = list(map(int, input().split()))
    f = False
    for x in X:
        if x in data:
            continue
        else:
            result.append(x)
            data.add(x)
            f=True
            break
    if not f:
        result.append(0)
for r in result:
    print(r)
