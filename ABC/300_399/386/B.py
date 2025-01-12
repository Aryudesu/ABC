def calc(S):
    count = 0
    f = False
    for s in S:
        if s != "0":
            if f:
                count += 1
                f = False
            count += 1
        else:
            if f:
                count += 1
                f = False
            else:
                f = True
    if f:
        count += 1
    return count

print(calc(input()))
