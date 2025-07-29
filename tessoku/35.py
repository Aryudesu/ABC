def calc(depth:int, A:list[int]) -> int:
    data = A
    for d in range(depth-1):
        next_data = []
        de = depth - d
        for i in range(depth - d - 1):
            if de % 2 == 0:
                next_data.append(max(data[i], data[i+1]))
            else:
                next_data.append(min(data[i], data[i+1]))
        data = next_data
    return data[0]

N = int(input())
A = [int(l) for l in input().split()]
print(calc(N, A))
