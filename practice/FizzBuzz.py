for i in range(1, int(input()) + 1):
    print("FizzBuzz" if not i % 15 else "Fizz" if not i %
          3 else "Buzz" if not i % 5 else i)
