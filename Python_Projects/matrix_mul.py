import numpy as np

A = np.array([[1, 2],
              [3, 4]])

B = np.array([[5, 6],
              [7, 8]])

print("Matrix A:\n", A)
print("Matrix B:\n", B)

# Matrix Addition
addition = A + B
print("\nMatrix Addition (A + B):\n", addition)

# Element-wise Multiplication
elementwise = A * B
print("\nElement-wise Multiplication (A * B):\n", elementwise)

# Matrix Multiplication (Dot Product)
dot_product = np.dot(A, B)
print("\nMatrix Multiplication (A dot B):\n", dot_product)

# Transpose of Matrix A
transpose_A = A.T
print("\nTranspose of Matrix A:\n", transpose_A)
