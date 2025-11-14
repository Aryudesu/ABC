def calc(S: str) -> list[list[int]]:
    data = []
    result = []
    for i in range(len(S)):
        if S[i] == "(":
            data.append(i)
        elif S[i] == ")":
            tmp = data.pop()
            result.append((i + 1, tmp + 1))
    result.sort()
    return result

S = input()
result = calc(S)
for r, l in result:
    print(l, r)
