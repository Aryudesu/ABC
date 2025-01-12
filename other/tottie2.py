N = 1000000000
with open("x-y_result.txt", mode="w") as f:
    f.write(f"{N}までのデータ\n")
    count = 0
    for i in range(1, N + 1):
        num = (i ** 2)
        num_str = str(num)
        for j in range(1, len(num_str)):
            a = int(num_str[:j])
            b = int(num_str[j:])
            if b == 0:
                continue
            if (a + b) ** 2 == num and f"{a}{b}" == num_str:
                count += 1
                f.write(f"({a}, {b})\n")
                print(f"({a}, {b})")
print(f"以上{count}個")
