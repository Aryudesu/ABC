def calc(start, T, p):
    now_node = {start}
    for t in range(T):
        new_node = set()
        for node in now_node:
            x = node[0]
            y = node[1]
            if abs(p[0] - (x + 1)) + abs(p[1] - y) <= T - (t + 1):
                new_node.add((x + 1, y))
            if abs(p[0] - (x - 1)) + abs(p[1] - y) <= T - (t + 1):
                new_node.add((x - 1, y))
            if abs(p[0] - x) + abs(p[1] - (y + 1)) <= T - (t + 1):
                new_node.add((x, y + 1))
            if abs(p[0] - x) + abs(p[1] - (y - 1)) <= T - (t + 1):
                new_node.add((x, y - 1))
        now_node = new_node
        # print(now_node)
    if p in now_node:
        return True
    return False


N = int(input())
plan = {0: (0, 0)}
t_max = 0
tm = [0]
for n in range(N):
    t, x, y = [int(l) for l in input().split()]
    plan[t] = (x, y)
    tm.append(t)
flag = True
for n in range(N):
    p_p = tm[n]
    p_n = tm[n + 1]
    if not calc(plan.get(p_p), tm[n + 1] - tm[n], plan.get(p_n)):
        flag = False
        break
print("Yes" if flag else "No")
