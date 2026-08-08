N = int(input())
S = "x" + input() + "x"
print(sum(S[idx-1] == "x" and S[idx] == "x" and S[idx+1] == "x" for idx in range(1, N+1)))
