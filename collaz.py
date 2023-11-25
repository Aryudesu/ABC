def col_count(num):
    result = [num]
    tmp = num
    while tmp != 1:
        t = tmp // 2 if tmp % 2 == 0 else tmp * 3 + 1
        result.append(t)
        tmp = t
    return result


def calc_max_length(N):
    result = []
    for n in range(1, N + 1):
        res = col_count(n)
        if len(result) < len(res):
            result = res
    return result


Num = int(input())
print(calc_max_length(Num))
