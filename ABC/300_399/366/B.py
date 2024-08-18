N = int(input())
S = []
ln = 0
ln_set = set()
for n in range(N):
    S.append(input())
S.reverse()

result = []
for idx in range(N):
    s = S[idx]
    L = len(s)
    for l in range(L):
        try:
            tmp = result[l]
        except Exception as e:
            result.append("")
        result[l] += "*" * (idx - len(result[l]))
        result[l] += s[l]
for r in result:
    print(r)
