def isOk(X1: int, Y1: int, R1: int, X2: int, Y2: int, R2: int)->bool:
    d = (X1 - X2) ** 2 + (Y1 - Y2) ** 2
    return d <= (R1 + R2) ** 2 and d >= (R2 - R1) ** 2

T = int(input())
result = []
for _ in range(T):
    X1, Y1, R1, X2, Y2, R2 = map(int, input().split())
    result.append("Yes" if isOk(X1, Y1, R1, X2, Y2, R2) else "No")
for r in result:
    print(r)
