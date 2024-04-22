from abc import ABCMeta, abstractmethod
from contextlib import contextmanager

# Define Qubit class for QuantumDevice
class Qubit(metaclass=ABCMeta):
    # Define Hadamard operation method
    @abstractmethod
    def h(self):
        pass

    # Define quantum NOT method
    @abstractmethod
    def x(self):
        pass

    # Define measuring method
    @abstractmethod
    def measure(self) -> bool:
        pass

    # Define reset method
    def reset(self):
        pass

# Define the QuantumDevice class
class QuantumDevice(metaclass=ABCMeta):
    # Define qubit allocation method
    @abstractmethod
    def allocate_qubit(self) -> Qubit:
        pass

    # Define qubit deallocation (cleanup) method
    @abstractmethod
    def deallocate_qubit(self, qubit: Qubit):
        pass

    # Define a context manager for using qubits
    @contextmanager
    def using_qubit(self):
        qubit = self.allocate_qubit()
        try:
            yield qubit
        finally:
            qubit.reset()
            self.deallocate_qubit(qubit)
