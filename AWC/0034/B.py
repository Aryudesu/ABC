N = int(input())
P = [int(l) - 1 for l in input().split()]
counter = 1
now = 0
while now != N-1:
    now = P[now]
    counter += 1
print(counter)
