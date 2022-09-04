N = int(input())
A = [int(l) for l in input().split()]
data = dict()
for a in range(N):
    tmp = data.setdefault(a % 200, [])
    tmp.append(a)
    data[a % 200] = tmp
res = 0
for key in data.keys():
    m = len(data[key])
    res += (m * (m-1))//2
print(res)
