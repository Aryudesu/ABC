N = int(input())
attack = 0
gold = 0
stack = []
for n in range(N):
    d, v = map(int, input().split())
    if d <= attack:
        gold += v
        attack += d
        while stack:
            d, v = stack.pop()
            if d <= attack:
                gold += v
                attack += d
            else:
                stack.append((d, v))
                break

    else:
        stack.append((d, v))
print(gold)
