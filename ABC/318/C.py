N, D, P = [int(l) for l in input().split()]
F = [int(l) for l in input().split()]
F.sort(reverse=True)
# print(F)
result = 0
tmp = 0
count = 0
for f in F:
    count += 1
    tmp += f
    if count % D == 0:
        if tmp > P:
            result += P
        else:
            result += tmp
        tmp = 0
        count = 0
if tmp > P:
    result += P
else:
    result += tmp
print(result)
