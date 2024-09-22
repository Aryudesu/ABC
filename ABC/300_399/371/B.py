N, M = [int(l) for l in input().split()]
memo = set()
result = []
for m in range(M):
    A, B = [l for l in input().split()]
    A = int(A)
    if not A in memo and B == "M":
        result.append("Yes")
        memo.add(A)
    else:
        result.append("No")
for r in result:
    print(r)
