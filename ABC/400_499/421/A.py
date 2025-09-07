N = int(input())
S = []
for n in range(N):
    S.append(input())
X, Y = input().split()
X = int(X)
print("Yes" if S[X-1] == Y else "No")
