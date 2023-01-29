N = int(input())
res = 0
for n in range(N):
    S = input()
    res += 1 if S == "For" else -1
print("Yes" if res > 0 else "No")
