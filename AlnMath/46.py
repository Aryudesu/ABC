def calc():
    R, C = [int(l) for l in input().split()]
    start = tuple([int(l) - 1 for l in input().split()])
    goal = tuple([int(l) - 1 for l in input().split()])
    field = [input() for r in range(R)]
    memo = {start}
    node = {start}
    result = 0
    while node:
        result += 1
        new_node = set()
        for y, x in node:
            for dy in range(-1, 2):
                for dx in range(-1, 2):
                    if dy == 0 and dx == 0:
                        continue
                    if dy != 0 and dx != 0:
                        continue
                    if field[y + dy][x + dx] == "#":
                        continue
                    tmp = tuple([y + dy, x + dx])
                    if tmp in memo:
                        continue
                    if tmp == goal:
                        return result
                    new_node.add(tmp)
                    memo.add(tmp)
        node = new_node
    return -1
print(calc())
