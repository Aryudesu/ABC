N = int(input())
Sdata = dict()
max_num = 0
for n in range(N):
    S = input()
    Sdata[S] = Sdata.get(S, 0) + 1
    max_num = max(max_num, Sdata[S])

data = []
for k in Sdata:
    data.append([Sdata.get(k, 0), k])
data.sort()
result = []
for dat in data:
    num, k = dat
    if num == max_num:
        print(k)

