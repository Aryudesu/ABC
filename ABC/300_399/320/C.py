rd = dict()


def calc(c, m, count):
    tmp = rd.get(c, [None, None, None])
    tmp[m] = True
    rd[c] = tmp
    return tmp[0] and tmp[1] and tmp[2]


M = int(input())
S1 = input()
S2 = input()
S3 = input()
result = M * 1000
for n in range(3 * M + 1):
    nn = n % M
    for m in range(3 * M + 1):
        mm = m % M
        for l in range(3 * M + 1):
            ll = l % M
            if S1[nn] == S2[mm] and S1[nn] == S3[ll] and n != m and n != l and m != l:
                tmp = max([n, m, l])
                if result > tmp:
                    result = tmp
if result == M * 1000:
    print(-1)
else:
    print(result)
