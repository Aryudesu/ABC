N = int(input())
print(*[int(l) for l in input().split() if int(l) % 2 == 0])
