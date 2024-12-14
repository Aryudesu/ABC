import pypyjit

pypyjit.set_param('max_unroll_recursion=-1')

COUNT = 0
def calc1(N, M, L, base, depth, memo):
    if depth == N:
        if memo[-1] <= M:
            global COUNT
            COUNT += 1
        return
    for i in range(base, depth * 10 + L + 1):
        memo[depth] = i
        calc1(N, M, L, i + 10, depth + 1, memo)

def calc(N, M, L, base, depth, memo):
    if depth == N:
        if memo[-1] <= M:
            print(*memo)
        return
    for i in range(base, depth * 10 + L + 1):
        memo[depth] = i
        calc(N, M, L, i + 10, depth + 1, memo)

N, M = [int(l) for l in input().split()]
L = M % 10
if L == 0:
    L = 10
memo = [None] * N
for i in range(1, L + 1):
    memo[0] = i
    calc1(N, M, L, i + 10, 1, memo)
print(COUNT)
for i in range(1, L + 1):
    memo[0] = i
    calc(N, M, L, i + 10, 1, memo)
