N = int(input())
init = {"M": 0, "A": 1, "R": 2, "C": 3, "H": 4}
data = [0, 0, 0, 0, 0]
for n in range(N):
    s = input()
    if s[0] in init:
        idx = init.get(s[0])
        data[idx] += 1
result = 0
for i in range(3):
    for j in range(i + 1, 4):
        for k in range(j + 1, 5):
            result += data[i] * data[j] * data[k]
print(result)
