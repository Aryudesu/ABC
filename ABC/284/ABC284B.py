T = int(input())
result = []
for t in range(T):
    N = int(input())
    A = [int(l) for l in input().split() if int(l) % 2]
    result.append(len(A))
for r in result:
    print(r)
