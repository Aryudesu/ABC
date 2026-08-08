def calc(K: int)->int:
    for n in range(1, 101):
        m = K * n
        S = str(m)
        if "00" in S:
            return m
    raise ValueError()
        


T = int(input())
result = []
for _ in range(T):
    K = int(input())
    result.append(calc(K))
for res in result:
    print(res)
