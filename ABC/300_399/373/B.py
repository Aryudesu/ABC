Alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
data = dict()
S = input()
for i in range(26):
    data[S[i]] = i
result = 0
prev = data["A"]
for i in range(1, 26):
    result += abs(data[Alphabet[i]] - prev)
    prev = data[Alphabet[i]]
print(result)
