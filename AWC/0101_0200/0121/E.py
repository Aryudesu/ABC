H, A, T = map(int, input().split())
S = input()
result = 0
isOk = False
for s in S:
    result += 1
    match s:
        case "A":
            A -= 1
            H -= 1
            if A >= H or H <= 1:
                H += 1
            else:
                A -= 1
                H -= 1
        case "C":
            A += 1
            if A >= H or H <= 1:
                H += 1
            else:
                A -= 1
                H -= 1
    if A <= 0 and H > 0:
        isOk = True
        break
print(result if isOk else -1)
