S = input()
data = []
for i in range(len(S)):
    newS = S[i:] + S[:i]
    data.append(newS)
data.sort()
print(data[0])
print(data[-1])
