def calc(N, S):
    for y in range(N):
        for x in range(y + 1, N):
            if S[y][x] == "W" and S[x][y] != "L":
                return False
            elif S[y][x] == "D" and S[x][y] != "D":
                return False
            elif S[y][x] == "L" and S[x][y] != "W":
                return False
    return True


N = int(input())
S = []
for n in range(N):
    S.append(input())
if calc(N, S):
    print("correct")
else:
    print("incorrect")
