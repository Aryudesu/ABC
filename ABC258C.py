N, Q = [int(l) for l in input().split()]
S = input()
idx = 0
res = []
for q in range(Q):
    query = [l for l in input().split()]
    if query[0] == "1":
        idx = (idx - int(query[1])) % N
    elif query[0] == "2":
        res.append(S[(idx + int(query[1]) - 1) % N])
for r in res:
    print(r)
