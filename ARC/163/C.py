# もうマヂムリ・・・・・・


def calc(N, data):
    if N == 2:
        print("No")
    if N < len(data):
        d = data[N]
        if d[1]:
            print("Yes")
            print(*list(d[0]))
        else:
            print("No")
    for n in range(len(data) - 1, N):
        tmp = set()
        bf = False
        dat = data[n]
        # print(dat)
        for da in dat[0]:
            if not dat[1]:
                data.append([tmp, False])
                break
            d = da
            if not bf:
                if not (d + 1) in dat[0] and not d * (d + 1) in dat[0]:
                    if d * (d + 1) <= 1000000000:
                        tmp.add(d + 1)
                        tmp.add(d * (d + 1))
                        bf = True
                    else:
                        tmp.add(d)
                else:
                    tmp.add(d)
            else:
                tmp.add(d)
        data.append([tmp, bf])
    if data[N][0]:
        print("Yes")
        print(*list(data[N][0]))
    else:
        print("No")


T = int(input())
data = [[{}, False], [{}, False], [[2, 2], True]]
for t in range(T):
    calc(int(input()), data)
