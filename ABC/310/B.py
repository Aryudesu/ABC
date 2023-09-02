def calc(Data, N):
    for i in range(N - 1):
        for j in range(i+1, N):
            a = Data[i][1]
            b = Data[j][1]
            if (a & b) == a:
                if len(a) < len(b) and Data[i][0] >= Data[j][0]:
                    return True
                elif len(a) <= len(b) and Data[i][0] > Data[j][0]:
                    return True
            elif (a & b) == b:
                if len(a) > len(b) and Data[i][0] <= Data[j][0]:
                    return True
                elif len(a) >= len(b) and Data[i][0] < Data[j][0]:
                    return True
    return False


N, M = [int(l) for l in input().split()]
Data = []
for n in range(N):
    PCF = [int(l) for l in input().split()]
    dat = []
    tmp = set()
    c = 0
    for pcf in PCF:
        if not c:
            dat.append(pcf)
            c = 1
        elif c == 1:
            c = 2
        elif c == 2:
            tmp.add(pcf)
    dat.append(tmp)
    Data.append(dat)
Data.sort(reverse=True)
# print(Data)
print("Yes" if calc(Data, N) else "No")
