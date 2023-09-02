S = input()
result = ""
ls = len(S)
for idx in range(ls//2):
    result = result + S[2*idx + 1] + S[2*idx]
print(result)
