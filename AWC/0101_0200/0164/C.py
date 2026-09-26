N, M = map(int, input().split())
S = list(map(int, input().split()))
D = list(map(int, input().split()))
S.sort()
D.sort()
result = 0
while S and D:
    d = D.pop()
    if S[-1] >= d:
        S.pop()
        result += 1
print(result)
