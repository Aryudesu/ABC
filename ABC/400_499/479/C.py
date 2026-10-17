N, W = map(int, input().split())
AB = []
for _ in range(N):
    a, b = map(int, input().split())
    AB.append((a, b))

result = 0
for mask in range(1 << N):
    score = 0
    weight = 0
    for n in range(N):
        a, b = AB[n]
        bt = 1 << n
        if mask & bt:
            score += a
            weight += b
    if weight <= W:
        result = max(result, score)
print(result)
