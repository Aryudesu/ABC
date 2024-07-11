def calc_m(S):
    sp = S.split("*")
    result = 1
    for s in sp:
        result *= int(s)
    return result


def calc_p(S):
    sp = S.split("+")
    result = 0
    for s in sp:
        if calc_m(s) != 0:
            result += 1
    return result


S = input()
print(calc_p(S))
