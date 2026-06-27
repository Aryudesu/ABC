N, Q = map(int, input().split())
S = list(map(int, input().split()))
data = list(map(int, input().split()))
heisa = [False] * N
result = []
for _ in range(Q):
    n, *query = map(int, input().split())
    match n:
        case 1:
            l, r, v = query
            for idx in range(l-1, r):
                data[idx] += v
        case 2:
            x = query[0]
            heisa[x-1] = True
        case 3:
            l, r = query
            res = 0
            for idx in range(l-1, r):
                if not heisa[idx] and data[idx] <= 0:
                    res += S[idx]
            result.append(res)
        case _:
            raise ValueError()

for r in result:
    print(r)
