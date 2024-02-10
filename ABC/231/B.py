N = int(input())
data = dict()
for n in range(N):
    S = input()
    data[S] = data.get(S, 0) + 1
res = ""
for k in data:
    if data.get(res, -1) < data.get(k, -1):
        res = k
print(res)
