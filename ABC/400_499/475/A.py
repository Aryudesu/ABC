S = input()
result = S[0]
for i in range(1, len(S)):
    result += "o" + S[i]
print(result)
