sc = [int(l) for l in input().split()]
s = "ABCDE"
data = []
for i in range(32):
    num = i
    bit = []
    name = ""
    score = 0
    for j in range(5):
        tmp = num % 2
        num //= 2
        score += sc[j] * tmp
        if tmp:
            name += s[j]
    if score == 0:
        continue
    data.append([-score, name])
data.sort()
# data.reverse()
for d in data:
    print(d[1])
