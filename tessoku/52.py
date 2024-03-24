Q = int(input())
data = []
result = []
pointer = 0
for q in range(Q):
    query = [l for l in input().split()]
    if query[0] == "1":
        data.append(query[1])
    elif query[0] == "2":
        result.append(data[pointer])
    elif query[0] == "3":
        pointer += 1
for r in result:
    print(r)
