def iter_map(x, K, f):
    d, p = {}, []
    for i in range(K):
        if x in d:
            l = i - d[x]
            return p[d[x] + (K - d[x]) % l]
        d[x] = i
        p.append(x)
        x = f(x)
    return x
