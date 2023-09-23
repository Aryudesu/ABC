def isKaibun(T):
    U = list(T)
    U.reverse()
    return list(T) == U


S = input()
result = 1
for i in range(len(S) - 1):
    for j in range(i, len(S)):
        if isKaibun(S[i: j + 1]):
            tmp = j - i + 1
            if tmp > result:
                result = tmp
print(result)
