N = int(input())
data = [int("1" * i) for i in range(1, 20)]
allNum = set()
for a in data:
    for b in data:
        for c in data:
            allNum.add(a + b + c)

allNum = list(allNum)
allNum.sort()
# print(allNum)
print(allNum[N-1])
