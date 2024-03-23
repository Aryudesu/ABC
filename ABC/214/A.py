N = int(input())
result = 0
if N <= 125:
    result = 4
elif N <= 211:
    result = 6
elif N <= 214:
    result = 8
else:
    raise Exception()
print(result)
