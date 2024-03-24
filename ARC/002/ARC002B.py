import datetime
year, month, day = [int(l) for l in input().split('/')]
da = datetime.datetime(year, month, day).date()
print(da)
while True:
    y = da.year
    m = da.month
    d = da.day
    if y % m != 0:
        t = y//m
        if t % d != 0:
            print(f'{y}/{m}/{d}')
            break
    da += 1    
