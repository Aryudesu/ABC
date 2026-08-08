from collections import defaultdict

N = int(input())
S = input()
vData = [0]
fData = [0]
data = [0]
v = 0
f = 0
for s in S:
    if s == "V":
        v += 1
        f += 0
    elif s == "F":
        v += 0
        f += 1
    elif s == "B":
        v += 1
        f += 1
    elif s == "N":
        v += 0
        f += 0
    else:
        raise ValueError()
    data.append(v - f) 
    vData.append(v)
    fData.append(f)
result = 0
counter = defaultdict(int)
for d in data:
    result += counter[d]
    counter[d] += 1
print(result)
