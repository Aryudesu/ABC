S = input()
data = dict()
for s in S:
    data[s] = data.get(s, 0) + 1
result = "a"
Alphabet = "abcdefghijklmnopqrstuvwxyz"
for a in Alphabet:
    if data.get(result, -1) < data.get(a, 0):
        result = a
print(result)
