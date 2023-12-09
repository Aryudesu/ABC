import cupy as cp
import numpy as np

A_cpu = np.random.randn(1000, 2000)
B_cpu = np.random.randn(2000, 3000)
A_gpu = cp.ndarray(memptr=A_cpu)
B_gpu = cp.ndarray(memptr=B_cpu)
AB_gpu = cp.dot(A_gpu, B_gpu)
AB_cpu2 = AB_gpu.get()
print(AB_cpu2)
