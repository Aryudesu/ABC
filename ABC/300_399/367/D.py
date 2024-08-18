N, M = [int(l) for l in input().split()]
A = [int(l) for l in input().split()]
# dat[距離をMで割った余り] = {0からn番目に到着するまでの距離がKeyになっている地点n}
dat = dict()
# dat[地点] = 距離をMで割った余り
key_dat = dict()
length = 0
result = 0
for n in range(2 * N - 1):
    k = n % N
    if n < N:
        tmp = dat.get(length % M, set())
        result += len(tmp)
        key = length % M
        tmp = dat.get(key, set())
        tmp.add(k)
        dat[key] = tmp
        key_dat[n] = key
    else:
        key = key_dat[k]
        tmp = dat.get(key, set())
        tmp.discard(k)
        dat[key] = tmp
        tmp = dat.get(length % M, set())
        result += len(tmp)
    length += A[k] % M
    # print(n, dat, key_dat)
print(result)
