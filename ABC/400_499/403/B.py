def calc(T, U):
    for i in range(len(T) - len(U) + 1):
        f = True
        for j in range(len(U)):
            # print(i, j)
            if T[i + j] == "?":
                continue
            if T[i+j] != U[j]:
                f = False
                break
        if f:
            return True
    return False

T = input()
U = input()
print("Yes" if calc(T, U) else "No")
