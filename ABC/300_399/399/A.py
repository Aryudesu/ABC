N = int(input())
S = input()
T = input()
result = 0
for i in range(N):
    if S[i] != T[i]:
        result += 1
print(result)
