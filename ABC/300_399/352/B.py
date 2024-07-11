S = input()
T = input()
i = 0
result = []
for j in range(len(T)):
    if T[j] == S[i]:
        i += 1
        result.append(j + 1)
print(*result)
