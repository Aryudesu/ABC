from collections import deque

Q = int(input())
data = deque()
result = []
for q in range(Q):
    query = input().split()
    if query[0] == "1":
        data.append(query[1])
    elif query[0] == "2":
        result.append(data[0])
    elif query[0] == "3":
        data.popleft()
for r in result:
    print(r)
