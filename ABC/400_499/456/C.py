S = input()
N = len(S)
res = 1
c = 1
for i in range(1, N):
    if S[i-1] == S[i]:
        c = 1
    else:
        c += 1
    res = (res + c) % 998244353
print(res)
