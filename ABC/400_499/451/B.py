N, M = map(int, input().split())
result = [0] * M
for n in range(N):
    a, b = map(int, input().split())
    result[a-1]-=1
    result[b-1]+=1
for r in result:
    print(r)
