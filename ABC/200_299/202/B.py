S = input()
result = []
for s in S:
    if s == "6":
        result.append("9")
    elif s == "9":
        result.append("6")
    else:
        result.append(s)
result.reverse()
print("".join(result))
