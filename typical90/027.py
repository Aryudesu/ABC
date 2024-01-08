N = int(input())
data = set()
result = []
for n in range(1, N + 1):
    S = input()
    if not S in data:
        data.add(S)
        result.append(n)
for r in result:
    print(r)
