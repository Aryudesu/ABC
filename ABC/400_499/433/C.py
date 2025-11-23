S = input()
prev = None
data = []
for s in S:
    if prev is None:
        prev = s
        count = 1
    else:
        if prev == s:
            count += 1
        else:
            data.append((int(prev), count))
            count = 1
            prev = s

data.append((int(prev), count))
result = 0
for i in range(len(data) - 1):
    a1, c1 = data[i]
    a2, c2 = data[i+1]
    if a1 + 1 == a2:
        result += min(c1, c2)
print(result)
