from fractions import Fraction
result = Fraction(0, 1)
print(result)
for i in range(1, 11):
    result += 2 * Fraction(1, i) * Fraction(4, 5) ** i
    print(float(result))
print(result)
print(float(result))
