def f(a: int):
    S = list(str(a))
    S.reverse()
    return int("".join(S))

X, Y = [int(l) for l in input().split()]
new_x = X
new_y = Y
for i in range(3, 11):
    new_y, new_x = f(new_x + new_y), new_y
    # print(new_y, new_x)
print(new_y)
