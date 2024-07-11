def calc5(N):
    if N == 0:
        return [0]
    result = []
    tmpN = N
    while tmpN:
        result.append(tmpN % 5)
        tmpN //= 5
    result.reverse()
    return result


def show(data):
    dat = ["0", "2", "4", "6", "8"]
    result = []
    for d in data:
        result.append(dat[d])
    print("".join(result))

N = int(input())
data = calc5(N-1)
# print(data)
show(data)
