N = int(input())
data = input().split()
for idx in range(N):
    data[idx] = int(data[idx].replace(".", ""))
result = 0
for t in data:
    if t > 370:
        result += t - 370
print(result)
