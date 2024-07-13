def make_bin_list(num, N = 0):
    result = []
    tmp = num
    while tmp:
        result.append(tmp % 2)
        tmp >>= 1
    if N > 0 and len(result) < N:
        for _ in range(N - len(result)):
            result.append(0)
    result.reverse()
    return result

S = list(input())
S.sort(reverse=True)
N = int("".join(S))
lenS = len(S)
result = -1
for i in range(2 ** lenS):
    a = []
    b = []
    bl = make_bin_list(i, lenS)
    okF = True
    for j in range(lenS):
        if bl[j] == 1:
            a.append(S[j])
        else:
            b.append(S[j])
    if len(a) > 0:
        if a[0] == "0":
            continue
    else:
        continue
    if len(b) > 0:
        if b[0] == "0":
            continue
    else:
        continue
    a_s = int("".join(a))
    b_s = int("".join(b))
    tmp = a_s * b_s
    if tmp > result:
        result = tmp
print(result)
