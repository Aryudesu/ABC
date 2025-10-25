def calc(A, B)-> bool:
    for num in range(A, B + 1):
        if 100 % num == 0:
            return True
    return False

A, B = map(int, input().split())
print("Yes" if calc(A, B) else "No")
