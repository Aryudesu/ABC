NL = list(input())
NL.reverse()
N1 = int(''.join(NL))
NL = list(str(N1))
NL.reverse()
N2 = int(''.join(NL))
print('Yes' if N1 == N2 else 'No')
