def calc(S):
    counter = 0
    for s in S:
        if s == "(":
            counter += 1
        elif s == ")":
            counter -= 1
        if counter < 0:
            return False
    return counter == 0

_ = input()
print("Yes" if calc(input()) else "No")
