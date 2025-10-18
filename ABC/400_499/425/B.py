def calc(N, A):
    data = set()
    for i in range(1, N + 1):
        data.add(i)
    for a in A:
        if a >= 0:
            if not a in data:
                return None
            data.discard(a)
    result = []
    for a in A:
        if a == -1:
            result.append(data.pop())
        else:
            result.append(a)
    return result


N = int(input())
A = [int(l) for l in input().split()]
res = calc(N, A)
if res is None:
    print("No")
else:
    print("Yes")
    print(*res)
