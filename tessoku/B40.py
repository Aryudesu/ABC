from collections import defaultdict
N = int(input())
A = list(map(int, input().split()))
data = defaultdict(int)
for a in A:
    data[a % 100] += 1

result = 0
for key in range(51):
    if key == 50:
        num = data[key]
        result += num * (num - 1)//2
    else:
        num1 = data[key]
        num2 = data[100 - key]
        result += (num1 * num2)
print(result)
