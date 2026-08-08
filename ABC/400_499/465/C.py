from collections import deque

N = int(input())
S = input()
result = deque()
reverseF = False
for idx in range(N):
    s = S[idx]
    if idx == 0:
        result.append(idx + 1)
        continue
    if reverseF:
        result.append(idx + 1)
    else:
        result.appendleft(idx + 1)
    if s == "o":
        reverseF = not reverseF
# print(result, reverseF)
displayResult = []
while result:
    if reverseF:
        displayResult.append(result.popleft())
    else:
        displayResult.append(result.pop())
print(*displayResult)
