def calc(B):
    result = 1
    while True:
        tmp = result ** result
        if tmp == B:
            return result
        if tmp > B:
            return -1
        result += 1


B = int(input())
print(calc(B))
