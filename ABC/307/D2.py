N = int(input())
S = input()
data = [0] * N
ddict = dict()
count = 0
for i in range(N):
    s = S[i]
    if s == "(":
        ddict[count] = i
        count += 1
    elif s == ")":
        count -= 1
        tmp = ddict.get(count)
        if not tmp is None:
            data[tmp] = 1
            data[i] = -1
count = 0
result = []
for i in range(N):
    count += data[i]
    if count == 0 and data[i] != -1:
        result.append(S[i])
print("".join(result))
