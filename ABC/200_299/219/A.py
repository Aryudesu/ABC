def calc(X: int)-> str:
    if 0 <= X < 40:
        return str(40 - X)
    if 40 <= X < 70:
        return str(70 - X)
    if 70 <= X < 90:
        return str(90 - X)
    return "expert"

X = int(input())
print(calc(X))
