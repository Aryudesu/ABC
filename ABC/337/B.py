def calc(S):
    mode = 0
    for s in S:
        if mode == 0:
            if s == "C":
                mode += 2
            elif s == "B":
                mode += 1
        elif mode == 1:
            if s == "A":
                return False
            elif s == "C":
                mode += 1
        elif mode == 2:
            if s == "B":
                return False
            elif s == "A":
                return False
    return True


S = input()
print("Yes" if calc(S) else "No")

