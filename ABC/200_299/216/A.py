X, Y = [int(l) for l in input().split(".")]
if 0 <= Y and Y <= 2:
    print(f"{X}-")
elif 3 <= Y and Y <= 6:
    print(f"{X}")
elif 7 <= Y and Y <= 9:
    print(f"{X}+")
