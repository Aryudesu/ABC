ONE_COUNT = 0
TWO_COUNT = 1

def calc(N, S):
    oc = 0
    tc = 0
    now_mode = ONE_COUNT
    result = 0
    for s in S:
        if s == "1":
            if now_mode == ONE_COUNT:
                oc += 1
            else:
                oc = 1
                tc = 0
                now_mode = ONE_COUNT
        elif s == "/":
            tc = 0
            now_mode = TWO_COUNT
            if oc == 0:
                result = max([result, 1])
                now_mode = ONE_COUNT
                oc = 0
                tc = 0
        elif s == "2":
            if now_mode == TWO_COUNT:
                tc += 1
                if tc <= oc:
                    result = max([result, tc * 2 + 1])
                else:
                    now_mode = ONE_COUNT
                    oc = 0
                    tc = 0
            else:
                now_mode = ONE_COUNT
                oc = 0
                tc = 0
        # print(s, oc, tc, now_mode)
    return result


N = int(input())
S = input()
print(calc(N, S))
