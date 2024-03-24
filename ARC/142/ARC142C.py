def calc(N):
    one = []
    two = []
    for n in range(N-2):
        s = ['?', str(1), str(n + 3)]
        print(' '.join(s))
        res = int(input())
        one.append(res)
    for n in range(N-2):
        s = ['?', str(2), str(n + 3)]
        print(' '.join(s))
        res = int(input())
        two.append(res)
    f = True
    min = N
    for n in range(N-2):
        if abs(one[n] - two[n]) != 1:
            f = False
        if min > one[n] + two[n]:
            min = one[n] + two[n]
    if f:
        if N == 4:
            if (one[0] == 1 and one[1] == 2) or (one[0] == 2 and one[1] == 1):
                return '! 3'
        return '! 1'
    return '! ' + str(min)

N = int(input())
print(calc(N))
