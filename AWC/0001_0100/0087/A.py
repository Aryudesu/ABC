T, X, Y = map(int, input().split())
A = input()
B = input()
result = 0
for a, b in zip(A, B):
    if a == "L":
        X -= 1
    elif a == "R":
        X += 1
    if b == "L":
        Y -= 1
    elif b == "R":
        Y += 1
    result += X == Y
print(result)
