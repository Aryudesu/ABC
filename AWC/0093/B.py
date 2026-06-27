N = int(input())
P = list(map(int, input().split()))
data = [False] * N
now = 0
while not data[now]:
    data[now] = True
    now = P[now] - 1
print(sum(data))
