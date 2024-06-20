import numpy as np
from bitarray import bitarray
from bitarray.util import count_n, zeros


class WaveletMatrix:
    def __init__(self, data, max_bits):
        self.max_bits = max_bits
        self.bit_arrays = [bitarray() for _ in range(max_bits)]
        self.zero_counts = [0] * max_bits
        self.build(data)

    def build(self, data):
        n = len(data)
        for level in range(self.max_bits):
            zeros = []
            ones = []
            for x in data:
                if (x >> (self.max_bits - level - 1)) & 1:
                    self.bit_arrays[level].append(1)
                    ones.append(x)
                else:
                    self.bit_arrays[level].append(0)
                    zeros.append(x)
            self.zero_counts[level] = len(zeros)
            data = zeros + ones

    def access(self, index):
        pos = index
        result = 0
        for level in range(self.max_bits):
            bit = self.bit_arrays[level][pos]
            result = (result << 1) | bit
            if bit == 0:
                pos = self.rank(0, pos, level)
            else:
                pos = self.zero_counts[level] + self.rank(1, pos, level)
        return result

    def rank(self, bit, index, level):
        if bit == 0:
            return self.bit_arrays[level][:index].count(0)
        else:
            return self.bit_arrays[level][:index].count(1)

# サンプルデータ
data = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
max_bits = max(data).bit_length()

# ウェーブレット行列の作成
wm = WaveletMatrix(data, max_bits)

# インデックス5の要素にアクセス
print("Access at index 5:", wm.access(5))
