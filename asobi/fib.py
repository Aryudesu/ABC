Fib = [0] * 200
Fib[1], Fib[2] = 1, 1
a, b = 1, 1
while b != 100:
    Fib[b + 1] = Fib[a] + Fib[b]
    a, b = a + 1, b + 1
print(Fib[100])
