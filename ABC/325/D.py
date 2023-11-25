N = int(input())
TD = []
Tdata = []
Tset = set()
Data = dict()
for n in range(N):
    T, D = [int(l) for l in input().split()]
    TD.append([T - 1, D])
    tmp = Data.get(T - 1)
    if tmp is None:
        tmp = [set(), set()]
    tmp[0].add(n)
    Data[T - 1] = tmp
    tmp = Data.get(T - 1 + D)
    if tmp is None:
        tmp = [set(), set()]
    tmp[1].add(n)
    Data[T + D - 1] = tmp
    if not (T - 1) in Tset:
        Tdata.append(T - 1)
        Tset.add(T - 1)
    if not (T + D - 1) in Tset:
        Tdata.append(T + D - 1)
        Tset.add(T + D - 1)
Tdata.sort()
TD.sort()
print(Tdata)
print(Data)
