A, B = [int(l) for l in input().split()]
result = 0
while True:
    A, B = (A, B) if A > B else (B, A)
    if A % B == 0:
        result += A // B - 1
        break
    result += A//B
    A = A % B
print(result)
