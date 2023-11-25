def calc(X, Y):
    if X < Y and X + 2 < Y:
        return False
    if X > Y and X - 3 > Y:
        return False
    return True


X, Y = [int(l) for l in input().split()]
print("Yes" if calc(X, Y) else "No")
