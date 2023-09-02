import sys
sys.setrecursionlimit(2*10**5)

N = int(input())
A = [int(l) - 1 for l in input().split()]
nodes = [0] * N
result = []


def calc(node):
    next_node = A[node]
    nodes[node] += 1
    if nodes[next_node] == 1:
        return next_node
    tmp = calc(next_node)
    if not tmp is None:
        return tmp
    else:
        nodes[node] += 1
    return False


def make_result(node, start):
    result.append(node + 1)
    next_node = A[node]
    if next_node == start:
        return
    make_result(next_node, start)


for n in range(N):
    if not nodes[n]:
        tmp = calc(n)
        if not tmp is None:
            make_result(tmp, tmp)
            print(len(result))
            print(*result)
            break
