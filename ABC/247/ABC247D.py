Q = int(input())
data = [[0, 0]]
pointer = 0
res = 0
result = []
for _ in range(Q):
    T, *p = [int(l) for l in input().split()]
    if T == 1:
        x, c = p
        if data[-1][0] == x:
            data[-1][1] += c
        else:
            data.append([x, c])
    elif T == 2:
        c = p
        tmpC = c
        while True:
            if data[pointer][1] > tmpC:
                data[pointer][1] -= tmpC
                res += data[pointer][0] * tmpC
                break
            elif data[pointer][1] == tmpC:
                res += data[pointer][0] * tmpC
                pointer += 1
                break
            else:
                res += data[pointer][0] * data[pointer][1]
                tmpC -= data[pointer][1]
        result.append(res)
