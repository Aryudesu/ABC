import sys


class Integer:
    def __init__(self, data=None) -> None:
        q = sys.stdin.readline().strip().split()
        self.content = tuple(map(int, q)) if len(q) > 1 else int(q[0]) if data==None else data

# datatype such as [1, 2, 3]
class IntegerList:
    def __init__(self, data=None) -> None:
        self.content = list(map(int, sys.stdin.readline().strip().split())) if data==None else data

    def indexList(self) -> list[int]:
        return sorted(range(len(self.content)), key=lambda i: self.content[i])
    
    def prefixSum1D(self) -> list[int]:
        prefixSum = [0]*(len(self.content)+1)
        for i in range(len(self.content)):
            prefixSum[i+1] = prefixSum[i] + self.content[i]

        return prefixSum
    
    def prefixSum1DReverse(self) -> list[int]:
        prefixSumReverse = [0]*(len(self.content)+1)
        for i in range(-1, -len(self.content)-1, -1):
            prefixSumReverse[i-1] = prefixSumReverse[i] - self.content[i]

        return prefixSumReverse

    def lowerBound(self, target) -> int: # target を挿入するべき最小の位置
        left, right = -1, len(self.content)
        while right - left > 1:
            middle = left + (right - left)//2
            if self.content[middle] < target: left = middle
            else: right = middle
        
        return right
        
    def upperBound(self, target) -> int: # target を挿入するべき最大の位置
        left, right = -1, len(self.content)
        while right - left > 1:
            middle = left + (right - left)//2
            if self.content[middle] <= target: left = middle
            else: right = middle
        
        return right

def solve():
    N,T = Integer().content
    A = IntegerList().content

    bingo = [[False]*N for _ in range(N)]

    for i in range(T):
        c,r = (A[i]-1)//N, (A[i]-1)%N
        # print(c,r)
        bingo[c][r] = True

        rflg, cflg, xflg, yflg = True, True, True, True
        for j in range(N):
            if bingo[j][r]==False: rflg = False
            if bingo[c][j]==False: cflg = False
            if bingo[j][j]==False: xflg = False
            if bingo[j][N-1-j]==False: yflg = False
            if rflg+cflg+xflg+yflg<1: break

        if rflg+cflg+xflg+yflg>0:
            # print(rflg, cflg, xflg, yflg)
            print(i+1)
            exit(0)

    print(-1)

if __name__ == "__main__":
    solve()

"""

ADBCACC


"""
