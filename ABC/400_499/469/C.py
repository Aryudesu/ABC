N = int(input())
S = input()
result = []
res = 0
p = 0
num = 0
for l in range(N):
    num += S[l] == "o"
    p = max(p, l)
    while p < N:
        if S[p] == "x":
            if num == 0:
                p -= 1
                break
            num -= 1
        else:
            num += 1
        p += 1
    result.append(p)
print(result)
