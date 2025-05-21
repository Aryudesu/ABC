def calc(B, C):
    if B == 0:
        return (C//2) + ((C-1)//2)
    return (C//2) + ((C-1)//2)

B, C = [int(l) for l in input().split()]
print(calc(B, C))
