L, R = [int(l) for l in input().split()]
S = input()
result = []
for i in range(len(S)):
    if i < L-1 or i >= R:
        result.append(S[i])
    else:
        result.append(S[R - 1 - (i-L+1)])
print("".join(result))
