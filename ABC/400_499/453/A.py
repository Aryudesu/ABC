N = int(input())
S = input()
count = 0
for i in range(N):
    if S[i] != "o":
        break
    count+=1
print(S[count:])
