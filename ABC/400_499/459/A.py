X = int(input())
S = "HelloWorld"
result = ""
for i in range(len(S)):
    if i == X-1:
        continue
    result += S[i]
print(result)
