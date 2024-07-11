def calc(S):
    memo = set()
    x = 0
    y = 0
    for s in S:
        memo.add((x, y))
        if s == "R":
            x += 1
        elif s == "L":
            x -= 1
        elif s == "U":
            y += 1
        elif s == "D":
            y -= 1
        if (x, y) in memo:
            return True
    return False


N = int(input())
S = input()
print("Yes" if calc(S) else "No")
