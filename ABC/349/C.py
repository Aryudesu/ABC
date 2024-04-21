def calc(S, T):
    lenS = len(S)
    lenT = len(T)
    count = 0
    for s in S:
        if s.upper() == T[count]:
            count += 1
            if count == 3:
                return True
    if count == 2:
        if T[-1] == "X":
            return True
    return False


S = input()
T = input()
print("Yes" if calc(S, T) else "No")
