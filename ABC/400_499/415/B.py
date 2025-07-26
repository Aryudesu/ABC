S = input()
data = []
for idx in range(len(S)):
    s = S[idx]
    if s == "#":
        data.append(idx + 1)
result = [[]]
for dat in data:
    if len(result[-1]) == 2:
        result.append([])
    result[-1].append(dat)
for r in result:
    print(f"{r[0]},{r[1]}")
