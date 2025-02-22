S = input()
result = list(S)
i = len(S) - 1
aFlag = False
while i >= 0:
    if i - 1 >= 0 and result[i] == "A" and result[i - 1] == "W":
        result[i] = "C"
        result[i-1] = "A"
    i -= 1
print("".join(result))
