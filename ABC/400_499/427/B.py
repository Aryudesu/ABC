def calc(num:int):
    S = str(num)
    res = 0
    for s in S:
        res += int(s)
    return res

N = int(input())
data = [1]
res = 0
for i in range(1, N + 1):
    tmp = calc(data[-1])
    data.append(res + tmp)
    res += tmp

print(data[-1])
