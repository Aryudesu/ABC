N = int(input())
cards = []
count = 0
xor = 0
data = dict()
result = []
for _ in range(N):
    query = input().split()
    q = query[0]
    if q == "PUT":
        c = int(query[1])
        cards.append(c)
        xor ^= c

    elif q == "REMOVE":
        c = cards.pop()
        xor ^= c
    elif q == "LOOK":
        if xor in data:
            result.append(data[xor] + 1)
        else:
            result.append(-1)
        data[xor] = count
        count += 1
    else:
        raise ValueError()
for r in result:
    print(r)
