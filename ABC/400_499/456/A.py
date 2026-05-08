def calc(X: int):
    for a in range(1, 7):
        for b in range(1, 7):
            for c in range(1, 7):
                if a + b + c == X:
                    return True
    return False

X = int(input())
print("Yes" if calc(X) else "No")
