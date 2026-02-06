def calc(N: int, C: int, S: list[str])->str:
    C = C - 1
    # なるべく下の方で空きマスにたどり着くことを考える
    data = [False] * N
    lowerWall = [-1] * N
    for x in range(N):
        for y in range(N):
            if S[- y - 1][x] == "#":
                if lowerWall[x] == -1:
                    lowerWall[x] = N-y-1
    # その列に最短で到達できる場所
    breakAble = [False] * N
    reachAble = [False] * N
    nodes = {C}
    breakAble[C] = True
    reachAble[C] = True
    for n in range(N-1):
        new_y = N - n - 2
        newNodes = set()
        for node in nodes:
            x = node
            for dx in range(-1, 2):
                new_x = x + dx
                # 範囲外
                if new_x < 0 or N <= new_x:
                    continue
                if S[new_y][new_x] == "#":
                    if not breakAble[new_x] and lowerWall[new_x] > new_y:
                        continue
                    if lowerWall[new_x] == new_y:
                        breakAble[new_x] = True
                newNodes.add(new_x)
        nodes = newNodes
    result = ["0"] * N
    for node in nodes:
        result[node] = "1"
    print("".join(result))


T = int(input())
for _ in range(T):
    N, C = map(int, input().split())
    S = [input() for _ in range(N)]
    calc(N, C, S)
