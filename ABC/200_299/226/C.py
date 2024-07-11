import sys

sys.setrecursionlimit(10**6)

def calc(TKA, node, memo):
    if node in memo:
        return 0
    t, k, a = TKA[node]
    result = 0
    for node_a in a:
        result += calc(TKA, node_a, memo)
    memo.add(node)
    result += t
    return result

N = int(input())
TKA = []
for n in range(N):
    T, K, *A = [int(l)-1 for l in input().split()]
    tmp = (T+1, K+1, A)
    TKA.append(tmp)
print(calc(TKA, N-1, set()))
