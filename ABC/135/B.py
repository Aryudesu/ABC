N = int(input())
P = [int(l) for l in input().split()]
count = 0
c = 1
for p in P:
    if c != p:
        count += 1
    c += 1
print("YES" if count <= 2 else "NO")
