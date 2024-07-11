S = input()
ST = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lst = len(ST)
stnum = {ST[i]: i for i in range(lst)}
res = 0
for s in S:
    res = res * lst + stnum.get(s) + 1
print(res)
