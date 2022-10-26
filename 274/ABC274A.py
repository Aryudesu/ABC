A, B = [int(l) for l in input().split()]
S = int((B*10000/A + 5)//10)
print(str(S//1000) + '.' + (str(S % 1000) + '000')[:3])
