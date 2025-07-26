def calc(N: int, ignore: set[int]) -> bool:
    node = {0}
    goal = 2 ** N - 1
    while node:
        next_node = set()
        for num in node:
            for i in range(N):
                m = 2**i
                if not (num & m) and not (num | m) in ignore:
                    if (num | m) == goal:
                        return True
                    next_node.add(num | m)
        node = next_node
    return False


T = int(input())
result = []
for t in range(T):
    N = int(input())
    S = input()
    ignore = set()
    for idx in range(len(S)):
        s = S[idx]
        if s == "1":
            num = idx + 1
            ignore.add(num)
    result.append("Yes" if calc(N, ignore) else "No")
for r in result:
    print(r)
