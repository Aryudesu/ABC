S = input()
result = 0
acgt = {"A", "C", "G", "T"}
for i in range(len(S)):
    tmp = 0
    for j in range(i, len(S)):
        if S[j] in acgt:
            tmp += 1
        else:
            break
    result = max(tmp, result)
print(result)
