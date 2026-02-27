def digit_sum(n: int) -> int:
    return sum(map(int, str(n)))

def calc(N: int, K: int)->int:
    graph = dict()
    for n in range(1, N + 1):
        m = n - digit_sum(n)
        graph[n] = m
    print(graph)

N, K = map(int, input().split())
calc(N, K)
