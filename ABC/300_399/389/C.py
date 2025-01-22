Q = int(input())
# [抜けが発生しない場合の頭の位置, 長さ]
data = []
index = 0
head = 0
result = []
for _ in range(Q):
    query = [int(l) for l in input().split()]
    if query[0] == 1:
        q, k = query
        if len(data) == 0:
            data.append([0, k])
        else:
            p, l = data[-1]
            data.append([p + l, k])
    elif query[0] == 2:
        head += data[index][1]
        index += 1
    elif query[0] == 3:
        q, k = query
        result.append(data[index + k - 1][0] - head)
    # print(data, head, index)
for r in result:
    print(r)
