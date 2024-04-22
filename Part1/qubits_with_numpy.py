import numpy as np

# Setting up |0> and |1>
ket0 = np.array([[1], [0]])
ket1 = np.array([[0], [1]])

# Defining |+>
ket_plus = (ket0 + ket1) / np.sqrt(2)
print(ket_plus)

# Defining Hadamard op
H = np.array([[1, 1], [1, -1]]) / np.sqrt(2)

# Using Hadamard op on |0> and |1>
print(f'Hadamard ket0: {H @ ket0}')
print(f'Hadamard ket1: {H @ ket1}')

# Representing the quantum NOT gate
X = np.array([[0, 1], [1, 0]])
print(f'NOT gate ket0: {X @ ket0}')
# This should return True, as .all() compares every value in each location
print(f'Compare NOT ket0 and ket1: {(X @ ket0 == ket1).all()}')
# Showing NOT doesn't change Hadamard ket0; should return True
print(f'NOT Hadamard ket0: {(X @ H @ ket0 == H @ ket0).all()}')