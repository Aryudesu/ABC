def calc(A, B, C):
    for i in range(24):
        if (C + i) % 24 == A:
            return True
        if (C + i) % 24 == B:
            break
    return False

A, B, C = [int(l) for l in input().split()]
print("Yes" if calc(A, B, C) else "No")
