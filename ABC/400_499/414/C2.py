class BaseConverter:
    """進数表記変換クラス"""
    def __init__(self):
        self.digits = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'

    def from_base(self, s: str, base: int) -> int:
        """任意の基数表記の文字列 s を10進整数に変換"""
        return int(s, base)

    def to_base(self, n: int, base: int) -> str:
        """10進整数 n を任意の基数 base の文字列に変換"""
        if n == 0:
            return '0'
        result = []
        while n > 0:
            result.append(self.digits[n % base])
            n //= base
        return ''.join(reversed(result))

    def convert(self, s: str, from_base: int, to_base: int) -> str:
        """任意の基数表記の文字列 s を、別の基数 to_base の文字列に変換"""
        n = self.from_base(s, from_base)
        return self.to_base(n, to_base)

def is_palindrome(data: str) -> bool:
    return data == data[::-1]


A = int(input())
N = int(input())
bc = BaseConverter()
result = 0
for i in range(10**6):
    s = str(i)
    num1 = int(s + s[::-1])
    num2 = int(s[:-1] + s[::-1])
    if num1 > N and num2 > N:
        break
    if num1 <= N and is_palindrome(bc.to_base(num1, A)):
        result += num1
    if num2 <= N and is_palindrome(bc.to_base(num2, A)):
        result += num2
print(result)
