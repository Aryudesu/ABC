S = input()
idx = 0
data = [0] * (len(S) + 3)
for s in S:
    if s == "A":
        if data[idx] != 0:
            idx += 1
        if data[idx] == 0:
            data[idx] += 1
        else:
            data[idx] = -1
    elif s == "B":
        if data[idx] != 1:
            idx += 1
        if data[idx] == 1:
            data[idx] += 1
        else:
            data[idx] = -2
    elif s == "C":
        if data[idx] != 2:
            idx += 1
        if data[idx] == 2:
            data[idx] = 0
            idx -= 1
            if idx < 0:
                idx = 0
        else:
            data[idx] = -3
#     print(s, idx, data)
# print(data)
result = []
for d in data:
    if d == -1:
        result.append("A")
    if d == -2:
        result.append("B")
    if d == -3:
        result.append("C")
    if d == 1:
        result.append("A")
    if d == 2:
        result.append("AB")
    if d == 3:
        result.append("ABC")
print("".join(result))