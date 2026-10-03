N, S = map(int, input().split())
W = list(map(int, input().split()))
result = 0
weight = 0
for w in W:
    weight += w
    if weight >= S:
        weight = 0
        result += 1
print(result)
