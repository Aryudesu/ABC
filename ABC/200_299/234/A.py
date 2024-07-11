def f(x):
    return x**2 + 2 * x + 3


def calc(t):
    return f(f(f(t) + t) + f(f(t)))

t = int(input())
print(calc(t))
