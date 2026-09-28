from collections import defaultdict

N, Q = map(int, input().split())
noTile = dict()
tile = dict()
alp = "abcdefghijklmnopqrstuvwxyz"
for c in alp:
    noTile[c] = set()
    tile[c] = set()
isTile = [False] * N
for n in range(N):
    noTile["a"].add(n)
for _ in range(Q):
    n, query = input().split()
    n = int(n)
    match n:
        case 1:
            X = int(query) - 1
            if isTile[X]:
                for key in noTile:
                    if X in tile[key]:
                        tile[key].discard(X)
                        noTile[key].add(X)
                        break
            else:
                for key in noTile:
                    if X in noTile[key]:
                        noTile[key].discard(X)
                        tile[key].add(X)
                        isIn = True
                        break
            isTile[X] = not isTile[X]
        case 2:
            C = query
            for key in noTile:
                if C == key:
                    continue
                tmp1 = noTile[C]
                tmp2 = noTile[key]
                if len(tmp1) >= len(tmp2):
                    tmp1.update(tmp2)
                    noTile[key] = set()
                    noTile[C] = tmp1
                else:
                    tmp2.update(tmp1)
                    noTile[key] = set()
                    noTile[C] = tmp2
        case _:
            raise ValueError()
result = [None] * N
for key in noTile:
    for idx in noTile[key]:
        result[idx] = key
for key in tile:
    for idx in tile[key]:
        result[idx] = key
print("".join(result))
