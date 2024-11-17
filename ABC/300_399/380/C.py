N, K = [int(l) for l in input().split()]
S = input()
zero = 0
zeroc = 0
one = 0
onec = 0
data = []
for s in S:
    if s == "0":
        if one > 0:
            onec += 1
            data.append([1, onec, one])
        one = 0
        zero += 1
    elif s == "1":
        if zero > 0:
            zeroc += 1
            data.append([0, zeroc, zero])
        one += 1
        zero = 0
if one > 0:
    onec += 1
    data.append([1, onec, one])
if zero > 0:
    zeroc += 1
    data.append([0, zeroc, zero])
result = ""
for i in range(len(data)):
    if data[i][0] == 1 and data[i][1] == K - 1:
        data[i][2] += data[i + 2][2]
    elif data[i][0] == 1 and data[i][1] == K:
        continue
    print(str(data[i][0]) * data[i][2], end="")
print()
