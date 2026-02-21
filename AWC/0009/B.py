N, S, C = map(int, input().split())
hp = S
result = 0
for n in range(N):
    h, p = map(int, input().split())
    if h <= hp:
        hp += p - h
    else:
        result += C
print(result)
