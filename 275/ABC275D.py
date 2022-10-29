def f(num, data):
    if num == 0:
        return 1
    d1 = data.get(num//2)
    d2 = data.get(num//3)
    if d1 == None:
        d1 = f(num//2, data)
        data[num//2] = d1
    if d2 == None:
        d2 = f(num//3, data)
        data[num//3] = d2
    return d1 + d2


data = {0: 1}
print(f(int(input()), data))
