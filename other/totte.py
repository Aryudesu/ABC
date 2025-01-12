def update(num, one, two, three, four, five, six):
    while num:
        a = num % 10
        num //= 10
        if a == 1:
            one += 1
        elif a == 2:
            two += 1
        elif a == 3:
            three += 1
        elif a == 4:
            four += 1
        elif a == 5:
            five += 1
        elif a == 6:
            six += 1
    return (one, two, three, four, five, six)

result = set()
N = 10
for a in range(N):
    for b in range(N):
        for c in range(N):
            for d in range(N):
                for e in range(N):
                    # for f in range(N):
                        one = 1
                        two = 1
                        three = 1
                        four = 1
                        five = 1
                        six = 1
                        one, two, three, four, five, six = update(a, one, two, three, four, five, six)
                        one, two, three, four, five, six = update(b, one, two, three, four, five, six)
                        one, two, three, four, five, six = update(c, one, two, three, four, five, six)
                        one, two, three, four, five, six = update(d, one, two, three, four, five, six)
                        one, two, three, four, five, six = update(e, one, two, three, four, five, six)
                        # one, two, three, four, five, six = update(f, one, two, three, four, five, six)
                        if a == one and b == two and c == three and d == four and e == five:
                            tmp = (a, b, c, d, e)
                            result.add(tmp)
print(result)
