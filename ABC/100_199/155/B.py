def calc():
    N = int(input())
    A = [int(l) for l in input().split()]
    for a in A:
        if a % 2 == 0:
            if a % 3 and a % 5:
                return "DENIED"
    return "APPROVED"

print(calc())
