result = []
data = [0] * 61
for x in range(60):
    for y in range(60):
        for z in range(60):
            num = 3*x + 2*y + z
            if num <= 60:
                data[num] += 1
                result.append((x,y,z))
print(data)
print(len(result))
