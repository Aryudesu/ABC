def calcAB(S):
    for x in range(10):
        for y in range(10):
            if S[x][y] == "#":
                return x + 1, y + 1

def calcCD(S):
    for x in range(1, 11):
        for y in range(1, 11):
            if S[-x][-y] == "#":
                return 10 - x + 1, 10 - y + 1

S = []
for n in range(10):
    S.append(input())

A, C = calcAB(S)
B, D = calcCD(S)
print(A, B)
print(C, D)
