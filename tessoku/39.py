N = int(input())
RL = []
for n in range(N):
    l, r = map(int, input().split())
    RL.append((r, l))
RL.sort()
now = 0
count = 0
for r, l in RL:
    if l < now:
        continue
    now = r
    count += 1
print(count)
