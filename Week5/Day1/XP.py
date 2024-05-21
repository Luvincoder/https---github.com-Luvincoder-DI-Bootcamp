import numpy as np

# Exercise 1

zeros_vector = np.zeros(10)

print(zeros_vector)

# Exercise 2

memory_size = zeros_vector.size * zeros_vector.itemsize
print(memory_size)

# Exercise 3

np.info(np.add)

# Exercise 4

vector_range = np.arange(10, 50)
print(vector_range)

# Exercise 5

vector_reverse = vector_range[::-1]
print(vector_reverse)

# Exercise 6
matrix_3x3 = np.arange(9).reshape(3, 3)
print(matrix_3x3)

# Exercise 7
non_zero_indices = np.nonzero([1, 2, 0, 0, 4, 0])
print(non_zero_indices)

# Exercise 8
identity_matrix = np.eye(3)
print(identity_matrix)

# Exercise 9
matrix_5x5 = np.tile(np.arange(5), (5, 1))
print(matrix_5x5)

# Exercise 10
vector_linspace = np.linspace(0.1, 0.9, 10)
print(vector_linspace)

# Exercise 11
random_vector = np.random.rand(10)
sorted_vector = np.sort(random_vector)
print(sorted_vector)

# Exercise 12
scalar_types = [np.int8, np.int32, np.int64, np.float32, np.float64]
for dtype in scalar_types:
    info = np.iinfo(dtype) if np.issubdtype(dtype, np.integer) else np.finfo(dtype)
    print(f"Minimum for {dtype.__name__}: {info.min}, Maximum: {info.max}")

# Exercise 13
float_array = np.array([1.1, 2.2, 3.3, 4.4], dtype=np.float32)
int_array = float_array.astype(np.int32)
print(int_array)

# Exercise 14
matrix = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
matrix_mean_subtracted = matrix - np.mean(matrix, axis=1, keepdims=True)
print(matrix_mean_subtracted)

# Exercise 15
array_to_sort = np.array([[1, 3], [2, 1], [4, 5]])
sorted_indices = np.argsort(array_to_sort[:, 1])
sorted_array = array_to_sort[sorted_indices]
print(sorted_array)

# Exercise 16
array_swap_rows = np.array([[0, 1, 2], [3, 4, 5], [6, 7, 8]])
array_swap_rows[0], array_swap_rows[1] = array_swap_rows[1], array_swap_rows[0]
print(array_swap_rows)

# Exercise 17
C = np.bincount([1, 2, 3, 1, 2, 1])
A = np.repeat(np.arange(len(C)), C)
print(A)

