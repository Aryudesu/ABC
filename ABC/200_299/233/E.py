X = [int(l) for l in list(input())]
s = 0
data = []
for x in X:
    s += x
    data.append(s)
for i in range(len(X) - 1):
    data[-(i+2)] += data[-(i+1)] // 10
    data[-(i+1)] = data[-(i+1)] % 10
for d in data:
    print(d, end="")
print()
