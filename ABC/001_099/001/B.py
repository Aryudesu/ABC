def calc(m):
    if m < 100:
        return str(0).zfill(2)
    elif 100 <= m <= 5000:
        return str(m//100).zfill(2)
    elif 6000 <= m <= 30000:
        return str(m//1000 + 50).zfill(2)
    elif 35000 <= m <= 70000:
        return str(((m//1000)-30)//5 + 80).zfill(2)
    else:
        return str(89).zfill(2)


m = int(input())
print(calc(m))
