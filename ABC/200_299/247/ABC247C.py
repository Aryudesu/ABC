def Sn(n):
    if n == 1:
        print("1", end="")
        return
    Sn(n-1)
    print(" ", end="")
    print(n, end="")
    print(" ", end="")
    Sn(n-1)

Sn(int(input()))
print()
