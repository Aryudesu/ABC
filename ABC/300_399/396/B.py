card = [0] * 100
Q = int(input())
for q in range(Q):
    query = [int(l) for l in input().split()]
    if query[0] == 1:
        q, x = query
        card.append(x)
    elif query[0] == 2:
        x = card.pop()
        print(x)
