def is_square(num: int):
    if (num**0.5).is_integer():
        return True
    return False
N = 10000

for i in range(1, N + 1):
    for j in range(N + 1):
        k = int(str(i**2) + str(j**2))
        if is_square(k):
            print(i, j, i**2, j**2, k, int(k**0.5))
