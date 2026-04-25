from sortedcontainers import SortedList

Q = int(input())
data = SortedList()
result = 0
for _ in range(Q):
    s, x = input().split()
    x = int(x)
    if s == "+":
        data.add(x)
    elif s == "-":
        mid = data[(len(data)-1)//2]
        if mid == x:
            result += 1
        # print(data, mid, result)
        data.discard(x)
    else:
        raise ValueError()
print(result)
