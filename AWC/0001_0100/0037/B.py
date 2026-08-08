L, R = map(int, input().split())
N = int(input())
data =[L, R+1]
result = []
for n in range(N):
    l, r = map(int, input().split())
    data = [max(data[0], l), min(data[1], r + 1)]
    if data[0] >= data[1]:
        data[0] = 0
        data[1] = 0
    # print(data)
    result.append(data[1] - data[0])
for r in result:
    print(r)
