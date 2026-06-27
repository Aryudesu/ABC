N, X = input().split()
N = int(N)
S = [input() for _ in range(N)]
row = {"A": 0, "B": 1, "C": 2, "D": 3, "E": 4}
r = row[X]
isOk = False
for n in range(N):
    if S[n][r] == "o":
        isOk = True
        break
print("Yes" if isOk else "No")
