a, b = [int(l) for l in input().split()]
print('Yes' if b - a == 1 or (b == 10 and a == 1) else 'No')
