def is_sq(num):
    for i in range(num):
        if i ** 2 == num:
            return True
        if i ** 2 > num:
            return False

for i in range(1, 1000):
    if is_sq(5 * (2*i + 1)):
        print(i)
