import itertools

N = int(input())
S = input()
button = "ABXY"
button_data = []
for b1 in button:
    for b2 in button:
        button_data.append(b1 + b2)

# print(button_data)

result = N + 1
for bd1 in button_data:
    for bd2 in button_data:
        tmp = S.replace(bd1, "L").replace(bd2, "R")
        if len(tmp) < result:
            result = len(tmp)
print(result)
