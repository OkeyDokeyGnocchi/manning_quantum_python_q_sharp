import numpy as np

# Setting up |0> and |1>
ket0 = np.array([[1], [0]])
ket1 = np.array([[0], [1]])

# Defining |+>
ket_plus = (ket0 + ket1) / np.sqrt(2)
print(ket_plus)

# Defining |->
ket_minus = (ket0 - ket1) / np.sqrt(2)
print(ket_minus)

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

# Exercise 3.2
## Check that |0> = (ket0 + ket1)/sqrt(2)
print(f'Verifying ket0 is superposition of |+> and |->: {(ket0 == (ket_plus + ket_minus)/np.sqrt(2)).all()}')

# Exercise 3.3
print("\nExercise 3.3")
## a) Calculate the probability of getting the measurement outcome |–⟩ when measuring the |0⟩ state in the |–⟩ direction
"|<-|0>|^2 == ((<-|0>) / np.sqrt(2)) ** 2"
print("a:")
print(f'{np.abs(ket_minus.conj().transpose() @ ket0) ** 2}')
print("b:")
print(f'{np.abs(ket_minus.conj().transpose() @ ket1) ** 2}')

# Exercise 3.4
print("\nExercise 3.4")
## If we had the ciphertext 10100101 and the key 00100110, what message was originally sent?
cipher = [bit == '1' for bit in '10100101']
key = [bit == '1' for bit in '00100110']
cleartext = [cipher_bit ^ key_bit for (cipher_bit, key_bit) in zip(cipher, key)]
print(f'{"".join("1" if bit else "0" for bit in cleartext)}')