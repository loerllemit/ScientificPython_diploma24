import time
import numpy as np

def matrix_mul(a, b):
    return [[sum(el_a * el_b for el_a, el_b in zip(row_a, col_b)) for col_b in zip(*b)]
        for row_a in a]

A = [[1,77,3],[4,5,6],[7,8,9]]
B = [[ 5., 10.],[15., 20.],[25., 30.]]

A_arr = np.array(A)
B_arr = np.array(B)


start_time = time.time()
matrix_mul(A,B)
end_time = time.time()
elapsed_time = end_time - start_time
print(f"Elapsed time: {elapsed_time} seconds")

start_time = time.time()
np.matmul(A_arr,B_arr)
end_time = time.time()
elapsed_time = end_time - start_time
print(f"Elapsed time: {elapsed_time} seconds")
