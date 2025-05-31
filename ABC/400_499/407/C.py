S = [int(l) for l in list(input())]
count = 0
base = 0
result = 0
for i in range(len(S)):
    tmp = (S[-(i + 1)] + base) % 10
    result += tmp
    base = (base - tmp) % 10
    result += 1
print(result)
