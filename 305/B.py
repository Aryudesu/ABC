data = [0, 3, 4, 8, 9, 14, 23]
p, q = [l for l in input().split()]
ST = "ABCDEFG"
print(abs(data[ST.index(p)] - data[ST.index(q)]))
