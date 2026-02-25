def calcFact(num: int)-> int:
    if num == 0:
        return 1
    result = 1
    for n in range(1, num + 1):
        result *= n
    return result

coins = [calcFact(n) for n in range(1, 11)]
coins.reverse()
result = 0
P = int(input())
for c in coins:
    if P == 0:
        break
    result += P // c
    P = P % c
print(result)
