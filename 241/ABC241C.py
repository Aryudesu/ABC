def searchResult(N, S):
    # 横
    for col in range(N):
        for row in range(N - 5):
            count = 0
            for idx in range(6):
                if S[col][row + idx] == "#":
                    count += 1
            if count >= 4:
                return "Yes"
    # 縦
    for col in range(N - 5):
        for row in range(N):
            count = 0
            for idx in range(6):
                if S[col + idx][row] == "#":
                    count += 1
            if count >= 4:
                return "Yes"
    # ＼
    for col in range(N - 5):
        for row in range(N - 5):
            count = 0
            for idx in range(6):
                if S[col + idx][row + idx] == "#":
                    count += 1
            if count >= 4:
                return "Yes"
    # ／
    for col in range(N - 5):
        for row in range(5, N):
            count = 0
            for idx in range(6):
                if S[col + idx][row - idx] == "#":
                    count += 1
            if count >= 4:
                return "Yes"
    return "No"


N = int(input())
S = []
for num in range(N):
    S.append(input())
print(searchResult(N, S))
