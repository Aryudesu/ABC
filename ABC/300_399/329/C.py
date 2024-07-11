N = int(input())
S = input()
result = dict()
count = 0
prev = ""
idx = 0
while idx < N:
    tmp = result.get(S[idx], 0)
    if S[idx] != prev:
        count = 1
    else:
        count += 1
    if count > tmp:
        result[S[idx]] = count
    prev = S[idx]
    idx += 1
res = 0
for k in result:
    res += result.get(k, 0)
print(res)
