N = int(input())
data = []
for n in range(N):
    S = input()
    data.append([len(S), S])
data.sort()
result = ""
for dat in data:
    result += dat[1]
print(result)
