N, Q = [int(l) for l in input().split()]
person = [False] * (N + 1)
result = []
n_c = 1
ced = 0
for q in range(Q):
    query = [int(l) for l in input().split()]
    if query[0] == 1:
        n_c += 1
    elif query[0] == 2:
        person[query[1]] = True
    elif query[0] == 3:
        for idx in range(ced + 1, n_c):
            if not person[idx]:
                result.append(idx)
                ced = idx - 1
                break
    else:
        raise Exception()
# print("")
for r in result:
    print(r)
