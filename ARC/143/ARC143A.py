def calc(Data):
    Data.sort()
    m = Data[2] - Data[1]
    k = Data[0] - m
    if k < 0:
        return -1
    return Data[2]


Data = [int(l) for l in input().split()]
print(calc(Data))
