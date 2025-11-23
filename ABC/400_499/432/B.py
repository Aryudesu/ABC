X = list(input())
X.sort()
firstNonZero = None
for i in range(len(X)):
    if X[i] != "0":
        firstNonZero = i
        break
if not firstNonZero is None:
    result = X[firstNonZero]
for i in range(len(X)):
    if i == firstNonZero:
        continue
    result += X[i]
print(result)
