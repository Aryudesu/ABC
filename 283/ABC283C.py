S = input()
prev_num = None
result = 0
for s in S:
    if s == "0":
        if prev_num == "0":
            prev_num = None
            result += 1
        else:
            prev_num = "0"
    else:
        if prev_num == "0":
            result += 1
        prev_num = s
        result += 1
    # print(s, prev_num, result)
if prev_num == "0":
    result += 1
print(result)
