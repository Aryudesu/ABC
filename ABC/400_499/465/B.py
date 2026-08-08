X, Y, L, R, A, B = map(int, input().split())
result = 0
for h in range(A, B):
    if L <= h < R:
        result += X
    else:
        result += Y
print(result)
