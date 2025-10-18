from collections import defaultdict

def calc(inputData: dict) -> str:
    data = set()
    for i in range(10000):
        a, b, c, d = list(str(i).zfill(4))
        data.add((a, b, c, d))

    numStr = "0123456789"
    for a, b, c, d in inputData["2"]:
        tmp = set()
        for num in numStr:
            if a != num:
                tmp.add((num, b, c, d))
            if b != num:
                tmp.add((a, num, c, d))
            if c != num:
                tmp.add((a, b, num, d))
            if d != num:
                tmp.add((a, b, c, num))
        data.intersection_update(tmp)
    
    for a, b, c, d in inputData["3"]:
        for num in numStr:
            data.discard((num, b, c, d))
            data.discard((a, num, c, d))
            data.discard((a, b, num, d))
            data.discard((a, b, c, num))
        data.discard((a, b, c, d))
    
    for a, b, c, d in inputData["1"]:
        tmp = set()
        tmp.add((a, b, c, d))
        data.intersection_update(tmp)

    if len(data) == 1:
        a, b, c, d = data.pop()
        return a + b + c + d
    else:
        return "Can't Solve"



N = int(input())
inputData = defaultdict(list)
for n in range(N):
    S, T = input().split()
    inputData[T].append(S)
print(calc(inputData))
