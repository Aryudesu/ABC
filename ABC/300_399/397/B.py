S = input()
result = 0
for i in range(len(S) - 1):
    if S[i] == S[i+1]:
        result += 1
if S[0] == "o":
    result += 1
if S[-1] == "i":
    result += 1
print(result)
