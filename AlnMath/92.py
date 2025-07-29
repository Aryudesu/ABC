N = int(input())
a = 1
result = 10**18
while a * a <= N:
    if N % a == 0:
        result = min(result, a + (N // a))
    a += 1
print(result*2)
