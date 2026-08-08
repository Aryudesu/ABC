# キリ番AWCだ
N, K = map(int, input().split())
A = list(map(int, input().split()))
print(sum(a%K==0 for a in A))
