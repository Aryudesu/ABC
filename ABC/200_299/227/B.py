data = set()
for a in range(1, 1000):
    for b in range(1, 1000):
        tmp = 3 * a + 4 * a * b + 3 * b
        data.add(tmp)
N = int(input())
S = [int(l) for l in input().split()]
result = 0
for s in S:
    if not s in data:
        result += 1
print(result)
