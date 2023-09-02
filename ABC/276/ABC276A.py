S = list(input())
lS = len(S)
res = -1
k = 0
for idx in range(lS):
    if S[idx] == 'a':
        res = idx + 1
print(res)
