def check(S):
    B = ['abcdefghijklmnopqrstuvwxyz', 'ABCDEFGHIJKLMNOPQRSTUVWXYZ']
    Sl = len(S)
    for idx in range(Sl):
        if S[idx] not in B[idx%2]:
            return 'No'
    return 'Yes'


print(check(input()))
