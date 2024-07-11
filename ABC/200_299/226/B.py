N = int(input())
a_data = set()
for n in range(N):
    l, *a = [int(l) for l in input().split()]
    a_data.add(tuple(a))
print(len(a_data))
