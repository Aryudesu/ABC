def isPalindromic(num: int)-> bool:
    origin = num
    tmp = 0
    while num > 0:
        tmp = tmp * 10 + num % 10
        num //= 10
    return tmp == origin

A, B = map(int, input().split())
count = 0
for num in range(A, B + 1):
    if isPalindromic(num):
        count += 1
print(count)
