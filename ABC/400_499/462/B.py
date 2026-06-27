N = int(input())
result = [[] for _ in range(N)]
for n in range(N):
    k, *A = list(map(int, input().split()))
    for a in A:
        result[a-1].append(n+1)
for res in result:
    print(len(res), *res)
