def calc(data: dict[tuple[int, int], int])->int:
    keys = list(data.keys())

N, P, Q, M = map(int, input().split())
data = dict()
for _ in range(N):
    l, r = map(int, input().split())
    data[(l, r)] = data.get((l, r), 0) + 1
for _ in range(M):
    x, a, b = map(int, input().split())
