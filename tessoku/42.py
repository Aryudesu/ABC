N, K = [int(l) for l in input().split()]
AB = []
for n in range(N):
    a, b = [int(l) for l in input().split()]
    AB.append(tuple([a, b]))
AB.sort()
result = 0
for i in range(N):
    a1, b1 = AB[i]
    bData = []
    for j in range(N):
        if i + j >= N:
            break
        a2, b2 = AB[i + j]
        if abs(a1 - a2) > K:
            break
        bData.append(b2)
    bData.sort()
    for k in range(len(bData)):
        inB1 = b1 == bData[k]
        count = 1
        for l in range(len(bData)):
            if k + l + 1 >= len(bData):
                break
            if abs(bData[k] - bData[k + l + 1]) > K:
                break
            if bData[k + l + 1] == b1:
                inB1 = True
            count += 1
        if inB1:
            result = max([result, count])
print(result)
