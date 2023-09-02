def calc(S, H, K, data):
    HP = H
    X, Y = 0, 0
    for s in S:
        if s == "R":
            X += 1
        elif s == "L":
            X -= 1
        elif s == "U":
            Y += 1
        elif s == "D":
            Y -= 1
        HP -= 1
        if HP < 0:
            return False
        if HP < K and (X, Y) in data:
            HP = K
            data.remove((X, Y))
    return True


N, M, H, K = [int(l) for l in input().split()]
S = input()
data = set()
for m in range(M):
    x, y = [int(l) for l in input().split()]
    data.add((x, y))
print("Yes" if calc(S, H, K, data) else "No")
