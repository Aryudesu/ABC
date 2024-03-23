S = input()
data = dict()
count = dict()
for idx in range(len(S)):
    s = S[idx]
    data[s] = idx + 1
    count[s] = count.get(s, 0) + 1
for k in data:
    if count[k] == 1:
        print(data[k])
