Q = int(input())
result = []
data = [""] * Q
pointer = -1
for q in range(Q):
    query = [l for l in input().split()]
    if len(query) == 2:
        title = query[1]
        data[pointer + 1] = title
        pointer += 1
    else:
        num = int(query[0])
        if pointer < 0:
            raise Exception()
        if num == 2:
            result.append(data[pointer])
        else:
            pointer -= 1
for r in result:
    print(r)
