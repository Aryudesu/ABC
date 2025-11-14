from sortedcontainers import SortedDict

def calc(N, K, X, A: list[int]) -> float:
    data = SortedDict()
    counter = K
    for a in A:
        k = a * (2**30)
        data[k] = data.get(k, 0) + 1
    while counter > 0:
        le, num = data.popitem()
        if counter - num >= 0:
            data[le//2] = data.get(le//2, 0) + num * 2
        else:
            data[le//2] = data.get(le//2, 0) + counter * 2
            data[le] = num - counter
        counter -= num
    co = 0
    while len(data) > 0:
        le, num = data.popitem()
        co += num
        if co >= X:
            return le/(2**30)
    raise Exception()



T = int(input())
result = []
for _ in range(T):
    N, K, X = map(int, input().split())
    A = list(map(int, input().split()))
    result.append(calc(N, K, X, A))

for r in result:
    print(r)
