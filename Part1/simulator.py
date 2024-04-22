import numpy as np
from interface import QuantumDevice, Qubit

# Set up some constants for use later
KET_0 = np.array([[1], [0]], dtype=complex)
H = np.array([[1, 1], [1, -1]], dtype=complex) / np.sqrt(2)
X = np.array([0, 1], [1, 0], dtype=complex) / np.sqrt(2)

# Define the class for simulated qubits
class SimulatedQubit(Qubit):
    def __init__(self):
        self.reset()

    # Define Hadamard op for self
    def h(self):
        self.state = H @ self.state

    # Define quantum NOT method
    def x(self):
        self.state = X @ self.state

    # Define measuring method
    def measure(self) -> bool:
        pr0 = np.abs(self.state[0, 0]) ** 2
        sample = np.random.random() <= pr0
        return bool(0 if sample else 1)

    # Define our reset method to reset to |0>
    def reset(self):
        self.state = KET_0.copy()

# Define the SingleQubitSimualtor class
class SingleQubitSimulator(QuantumDevice):
    # Get a simulated qubit as available
    avail_qubits = [SimulatedQubit()]

    # Define method for allocating qubits
    def allocate_qubit(self) -> SimulatedQubit:
        # If avail qubit found, pop from list
        if self.avail_qubits:
            return self.avail_qubits.pop()

    # Define method for deallocation of qubits
    def deallocate_qubit(self, qubit: SimulatedQubit):
        self.avail_qubits.append(qubit)
