def calc(S, T, X):
    sw = False
    for i in range(48):
        if (i % 24) == S:
            sw = True
        elif (i % 24) == T:
            sw = False
        if sw and (i % 24) == X:
            return True
    return False

S, T, X = [int(l) for l in input().split()]
print("Yes" if calc(S, T, X) else "No")
