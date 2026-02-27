from typing import Tuple

def getLR(N: int, X: int, A: str)->Tuple[int, int]:
    l, r = -1, -1
    f = False
    xF = False
    for i in range(N):
        if i+1 == X:
            xF = True
        if A[i] == "." and not f:
            l = i
            f = True
        elif A[i] == "#":
            r = i-1
            f = False
            if xF:
                break
    if r == -1:
        r = N-1
    return (l, r)


N, X = map(int, input().split())
A = input()
l, r = getLR(N, X, A)
result = ""
for i in range(N):
    if l <= i <= r:
        result += "@"
    else:
        result += A[i]
print(result)
