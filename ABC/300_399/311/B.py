N, D = [int(l) for l in input().split()]
data = [True] * D
for n in range(N):
    S = input()
    for d in range(D):
        if S[d] == "x":
            data[d] = False
result = 0
count = 0
for d in data:
    if d:
        count += 1
    else:
        if result < count:
            result = count
        count = 0
if result < count:
    result = count
print(result)
