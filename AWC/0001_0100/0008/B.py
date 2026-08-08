N = int(input())
H = list(map(int, input().split()))
m = -1
result = 0
for h in H:
    if m < h:
        m = h
        result += 1
print(result)
