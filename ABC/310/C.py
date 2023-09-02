N = int(input())
Data = set()
same = 0
for n in range(N):
    dat = list(input())
    a = "".join(dat)
    dat.reverse()
    b = "".join(dat)
    if a == b and (not a in Data):
        same += 1
    Data.add(a)
    Data.add(b)
print((len(Data) + same)//2)
