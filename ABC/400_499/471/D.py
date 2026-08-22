from sortedcontainers import SortedList

Q, V = map(int, input().split())
data = SortedList()
result = []
for _ in range(Q):
    n, *query = map(int, input().split())
    match n:
        case 1:
            t, w = query
            data.add(w-t)
        case 2:
            t = query[0]
            if data:
                w = data.pop(-1)
                result.append(min(V, w + t))
            else:
                result.append(-1)
        case _:
            raise ValueError()
    # print(data)
print(*result, sep="\n")
