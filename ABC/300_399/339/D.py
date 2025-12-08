def enc(y1, x1, y2, x2, base):
    return y1 * (base ** 3) + x1 * (base ** 2) + y2 * base + x2

def dec(num, base):
    return num // (base ** 3), (num % (base ** 3)) // (base ** 2), (num % (base ** 2)) // base, num % base


def calc(N: int, S: list[str])-> int:
    INF = N ** 4
    P = []
    dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    for h in range(N):
        for w in range(N):
            if S[h][w] == "P":
                P.append(h)
                P.append(w)
    py1, px1, py2, px2 = P
    node = enc(py1, px1, py2, px2, N)
    nodes = {node}
    memo = {node}
    count = 0
    while nodes:
        count += 1
        nextNodes = set()
        for node in nodes:
            py1, px1, py2, px2 = dec(node, N)
            for dy, dx in dirs:
                newPy1 = py1 + dy
                newPx1 = px1 + dx
                if not (0 <= newPy1 < N and 0 <= newPx1 < N):
                    newPy1 = py1
                    newPx1 = px1
                if S[newPy1][newPx1] == "#":
                    newPy1 = py1
                    newPx1 = px1
                newPy2 = py2 + dy
                newPx2 = px2 + dx
                if not (0 <= newPy2 < N and 0 <= newPx2 < N):
                    newPy2 = py2
                    newPx2 = px2
                if S[newPy2][newPx2] == "#":
                    newPy2 = py2
                    newPx2 = px2
                e = enc(newPy1, newPx1, newPy2, newPx2, N)
                if e in memo:
                    continue
                if newPy1 == newPy2 and newPx1 == newPx2:
                    return count
                memo.add(e)
                nextNodes.add(e)
        nodes = nextNodes
    return -1

N = int(input())
S = [input() for _ in range(N)]
print(calc(N, S))
