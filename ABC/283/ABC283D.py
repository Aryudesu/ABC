def calc(S):
    count = 0
    result = True
    box = {}
    box[0] = set()
    for s in S:
        if s == "(":
            count += 1
            box[count] = set(box[count-1])
        elif s == ")":
            count -= 1
        else:
            tmp = box.get(count)
            if s in tmp:
                result = False
            tmp.add(s)
    if count != 0:
        raise Exception
    return result


print("Yes" if calc(input()) else "No")
