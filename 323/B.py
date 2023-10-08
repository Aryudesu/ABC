N = int(input())
person = [[0, n + 1] for n in range(N)]
for n in range(N):
    S = input()
    for m in range(N):
        person[n][0] -= 1 if S[m] == "o" else 0
person.sort()
result = []
for p in person:
    result.append(p[1])
print(*result)
