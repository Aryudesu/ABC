def calc():
    data = dict()
    data["1"] = input()
    data["2"] = input()
    data["3"] = input()
    T = input()
    for t in T:
        print(data[t], end="")
    print()

calc()
