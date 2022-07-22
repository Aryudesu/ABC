a = [int(l) for l in input().split()]
b = sorted(a)
if a[1] == b[1]:
    print('Yes')
else:
    print('No')
