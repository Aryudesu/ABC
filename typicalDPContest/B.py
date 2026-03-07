from collections import defaultdict

N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
dp = defaultdict(int)
dp[(N, M)] = 0

