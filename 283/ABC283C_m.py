S = input()
result = 0
idx = len(S) - 1
while idx >= 0:
    if idx > 0 and S[idx] == "0" and S[idx - 1] == "0":
        idx -= 1
    idx -= 1
    result += 1
print(result)
