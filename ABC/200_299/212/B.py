def isWeak(X: list[int]) -> bool:
    if len(set(X)) == 1:
        return True
    for i in range(3):
        if (X[i] + 1) % 10 != X[i+1]:
            return False
    return True

X = list(map(int, list(input())))
print("Weak" if isWeak(X) else "Strong")
