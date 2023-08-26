M = int(input())
D = [int(l) for l in input().split()]
days = (sum(D)+1)//2
month = 1
day = 0
result = None
for d in D:
    if day + d >= days:
        result = days - day
        break
    day += d
    month += 1
if result is None:
    raise Exception()
print(month, result)
