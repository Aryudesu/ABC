r_num, c_num = dict(), dict()
r_data, c_data = [], []
r_count, c_count = 0, 0
data = dict()
N = int(input())
for n in range(N):
    r, c, x = [int(l) for l in input().split()]
    r_tmp = r_num.get(r)
    if r_tmp is None:
        r_data.append([x, r_count])
        r_num[r] = r_count
        r_tmp = r_count
        r_count += 1
    else:
        r_data[r_tmp][0] += x

    c_tmp = c_num.get(c)
    if c_tmp is None:
        c_data.append([x, c_count])
        c_num[c] = c_count
        c_tmp = c_count
        c_count += 1
    else:
        c_data[c_tmp][0] += x

    data[(r_tmp, c_tmp)] = x
r_data.sort(reverse=True)
c_data.sort(reverse=True)
result = 0
for r in r_data:
    f = False
    for c in c_data:
        tmp = r[0] + c[0]
        t_d = data.get((r[1], c[1]))
        if t_d is None:
            if result < tmp:
                result = tmp
                f = True
            break
        else:
            tmp = tmp - t_d
            if result < tmp:
                result = tmp
    if f:
        break
print(result)
