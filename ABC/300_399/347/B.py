S = input()
data = set()
for i in range(len(S)):
    for j in range(i, len(S)):
        data.add(S[i:j+1])
# print(data)
print(len(data))
