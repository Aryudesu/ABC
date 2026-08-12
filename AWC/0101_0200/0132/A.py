N, P = map(int, input().split())
H = list(map(int, input().split()))
hp = P
result = 0
for h in H:
    if hp >= h:
        hp -= h
        result += 1
    else:
        hp += h
print(result)
