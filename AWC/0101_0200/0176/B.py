N = int(input())
S = input()
print(sum(S[idx] == "C" and S[idx+1] == "A" for idx in range(N-1)))
