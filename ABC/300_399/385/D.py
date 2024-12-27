from sortedcontainers import SortedSet

N, M, Sx, Sy = [int(l) for l in input().split()]
Ydata = dict()
Xdata = dict()
for n in range(N):
    x, y = [int(l) for l in input().split()]
    tmp: SortedSet = Ydata.get(y, SortedSet())
    tmp.add(x)
    Ydata[y] = tmp
    tmp: SortedSet = Xdata.get(x, SortedSet())
    tmp.add(y)
    Xdata[x] = tmp
# print(Ydata)
# print(Xdata)
result = 0
for m in range(M):
    D, C = input().split()
    C = int(C)
    if D == "U":
        new_x = Sx
        new_y = Sy + C
        l = Sy
        r = new_y
    elif D == "D":
        new_x = Sx
        new_y = Sy - C
        l = new_y
        r = Sy
    elif D == "L":
        new_x = Sx - C
        new_y = Sy
        l = new_x
        r = Sx
    elif D == "R":
        new_x = Sx + C
        new_y = Sy
        l = Sx
        r = new_x
    if D == "U" or D == "D":
        tmp = Xdata.get(Sx)
        if tmp is None:
            Sx = new_x
            Sy = new_y
            continue
        r_idx = tmp.bisect_right(r)
        l_idx = tmp.bisect_left(l)
        for i in range(r_idx, l_idx - 1, -1):
            if i >= len(tmp):
                continue
            if i < 0:
                break
            if tmp[i] > r:
                continue
            if tmp[i] < l:
                break
            Ydata[tmp[i]].discard(Sx)
            tmp.discard(tmp[i])
            result += 1
        if new_y in tmp:
            tmp.discard(new_y)
            Ydata[new_y].discard(Sx)
            result += 1
    elif D == "L" or D == "R":
        tmp = Ydata.get(Sy)
        if tmp is None:
            Sx = new_x
            Sy = new_y
            continue
        r_idx = tmp.bisect_right(r)
        l_idx = tmp.bisect_left(l)
        for i in range(r_idx, l_idx - 1, -1):
            if i >= len(tmp):
                continue
            if i < 0:
                break
            if tmp[i] > r:
                continue
            if tmp[i] < l:
                break
            Xdata[tmp[i]].discard(Sy)
            tmp.discard(tmp[i])
            result += 1
        if new_x in tmp:
            tmp.discard(new_x)
            Xdata[new_x].discard(Sy)
            result += 1
    Sx = new_x
    Sy = new_y
print(Sx, Sy, result)
