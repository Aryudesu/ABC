S = input()
data = dict()
for s in S:
    data[s] = data.get(s, 0) + 1
data2 = dict()
for k in data:
    num = data.get(k, 0)
    tmp = data2.get(num, [])
    tmp.append(k)
    data2[num] = tmp
result = True
for k in data2:
    tmp = data2.get(k, [])
    if len(tmp) != 0 and len(tmp) != 2:
        result = False
print("Yes" if result else "No")
