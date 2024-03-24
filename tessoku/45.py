def colorNum(C):
    if C == "W":
        return 0
    if C == "B":
        return 1
    if C == "R":
        return 2
    raise Exception()

def calc(A, C):
    tmp = 0
    for a in A:
        tmp = (tmp + colorNum(a)) % 3
    return tmp == colorNum(C)

N, C = [l for l in input().split()]
A = input()
print("Yes" if calc(A, C) else "No")
