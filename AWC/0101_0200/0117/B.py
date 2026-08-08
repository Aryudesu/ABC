N, Q = map(int, input().split())
C = list(map(int, input().split()))
data = [0] * N
result = []
idx = 0
for _ in range(Q):
    n, q = input().split()
    match n:
        case "1":
            v = int(q)
            V = v
            while V > 0 and idx < N:
                d = min(C[idx]-data[idx], V)
                data[idx] += d
                V-=min(d, V)
                if data[idx] == C[idx]:
                    idx += 1
        case "2":
            k = int(q)
            result.append(data[k-1])
        case _:
            raise ValueError()

for res in result:
    print(res)
