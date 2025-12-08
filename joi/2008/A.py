N = int(input())
data = []
for n in range(N):
    color = int(input())
    if n % 2 == 0:
        data.append((color, 1))
        continue
    if len(data) == 1:
        pc1, num1 = data.pop()
        if pc1 == color:
            data.append((pc1, num1 + 1))
        else:
            data.append((pc1, num1))
            data.append((color, 1))
    elif len(data) == 0:
        data.append((color, 1))
    elif len(data) >= 2:
        pc1, num1 = data.pop() # 一番右の色
        pc2, num2 = data.pop() # 一番右から1つ隣の色
        if color == pc1:
            data.append((pc2, num2))
            data.append((pc1, num1 + 1))
        else:
            data.append((color, num1 + num2 + 1))
    print(data)
print(data)
