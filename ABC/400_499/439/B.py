def calc(num: int)->int:
    result = 0
    while num:
        result += (num % 10) ** 2
        num //= 10
    return result

N = int(input())
data = set()
num = N
while True:
    data.add(num)
    num = calc(num)
    if num in data:
        break
print("Yes" if num == 1 else "No")
