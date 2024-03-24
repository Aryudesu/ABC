def calc(m):
    if m < 100:
        return "00"
    elif 100 <= m and m <= 5000:
        return str(m//100)
    elif 6000 <= m and m <= 30000:
        return ""


m = int(input())
