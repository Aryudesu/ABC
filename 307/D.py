N = int(input())
S = input()
data = [[]]
count = 0
midx = 0
idx = 0
for s in S:
    if s == "(":
        idx += 1
        if idx > midx:
            data.append([s])
            midx = idx
        else:
            data[idx] = [s]
    elif s == ")":
        if idx > 0:
            idx -= 1
        else:
            data[0].append(s)
    else:
        data[idx].append(s)
result = ""
for i in range(idx + 1):
    print("".join(data[i]), end="")
print()
