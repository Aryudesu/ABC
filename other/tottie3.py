def isAllNum(data):
    s = set(list(data))
    return len(s) == 10

result = []
count = 0
i = 11110
while True:
    i += 1
    num = (i ** 2)
    num_str = str(num)
    for j in range(1, len(num_str)):
        a = int(num_str[:j])
        b = int(num_str[j:])
        if b == 0:
            continue
        if (a + b) ** 2 == num and f"{a}{b}" == num_str:
            # print(f"({a}, {b}) ", end="")
            if isAllNum(num_str):
                # print("OK")
                print(f"({a}, {b})")
                print(a, b, (a + b) ** 2)
                result.append(tuple([a, b]))
                count += 1
                if count == 10:
                    print(result)
                    exit()
            else:
                # print("NG")
                pass
