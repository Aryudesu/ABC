def calc(W):
    data = {"and", "not", "that", "the", "you"}
    for w in W:
        if w in data:
            return True
    return False


N = int(input())
W = [l for l in input().split()]
print("Yes" if calc(W) else "No")
