N = int(input())
A = list(map(int, input().split()))
data = set()
for a in A:
    if a in data:
        data.discard(a)
    else:
        data.add(a)
print(sum(data))
