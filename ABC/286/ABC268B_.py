N = int(input())
S = input()
res, prev = '', ''
for s in S:
    res += 'ya' if prev == 'n' and s == 'a' else s
print(res)
