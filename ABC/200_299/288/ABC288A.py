N = int(input())
result = []
for n in range(N):
    result.append(sum([int(l) for l in input().split()]))
for r in result:
    print(r)
