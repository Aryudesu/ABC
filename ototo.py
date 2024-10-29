from itertools import permutations

data = [1, 2, 3, 4, 5, 6, 7, 9]

for dat in permutations(data):
    if dat[0] * dat[1] == dat[2] * 10 + dat[3] and dat[4] * dat[5] == dat[6] * 10 + dat[7]:
        print(dat)
