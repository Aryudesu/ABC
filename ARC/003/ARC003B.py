data = []
N = int(input())
for n in range(N):
    data.append(list(input())[::-1])
data.sort()
result = []
for dat in data:
    result.append("".join(dat[::-1]))
for r in result:
    print(r)
