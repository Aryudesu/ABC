def calc(K):
    num = 0
    data = set()
    count = 0
    while True:
        count += 1
        num = (num * 10 + 7) % K
        if num in data:
            return -1
        data.add(num)
        if num == 0:
            return count

K = int(input())
print(calc(K))
