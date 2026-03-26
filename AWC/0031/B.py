def getBest2(data: list[int], e: int = -1)->list[int]:
    result = [e, e]
    for dat in data:
        if result[0] < dat:
            result[1] = result[0]
            result[0] = dat
        elif result[1] < dat:
            result[1] = dat
    return result

N, T = map(int, input().split())
result = 0
for t in range(T):
    s = map(int, input().split())
    b2 = getBest2(s)
    if b2[0] >= 2 * b2[1]:
        result += 1
print(result)
