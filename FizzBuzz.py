N = 100
for n in range(1, N + 1):
    print(((n if n % 5 else "Buzz") if n % 3 else "Fizz") if n % 15 else "FizzBuzz")
