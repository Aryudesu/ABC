N = int(input())
taka = [0, 0]
dokuF = False
XY = []
for n in range(N):
    new_taka = [0, 0]
    X, Y = [int(l) for l in input().split()]
    if X:
        tmp = taka[0] + Y
        if taka[1] < tmp:
            taka[1] = tmp
        dokuF = True
    else:
        tmp = taka[0] + Y
        if dokuF:
            if taka[1] + Y > tmp:
                tmp = taka[1] + Y
        if tmp > taka[0]:
            taka[0] = tmp
    # print(taka)
result = taka[0]
if dokuF:
    if result < taka[1]:
        result = taka[1]
print(result)
