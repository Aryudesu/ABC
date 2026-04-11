def calc(M: int, D: int)->bool:
    if M == 1 and D == 7:
        return True
    if M == 3 and D == 3:
        return True
    if M == 5 and D == 5:
        return True
    if M == 7 and D == 7:
        return True
    if M == 9 and D == 9:
        return True
    return False

M, D = map(int, input().split())
print("Yes" if calc(M, D) else "No")
