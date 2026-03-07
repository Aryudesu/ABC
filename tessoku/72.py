from sortedcontainers import SortedList

H, W, K = map(int, input().split())
C = [input() for _ in range(H)]
rowData = SortedList()
colData = SortedList()
