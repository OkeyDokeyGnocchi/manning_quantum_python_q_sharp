from interface import QuantumDevice, Qubit
from qrng import qrng
from simulator import SingleQubitSimulator

# Original insecure method, uses outright NOT gate
def prep_classical_message(bit: bool, q: Qubit) -> None:
    if bit:
        q.x()

def remote_measure(q: Qubit) -> bool:
    return q.measure()

def send_classical_message(device: QuantumDevice, bit: bool) -> None:
    with device.using_qubit() as q:
        prep_classical_message(bit, q)
        result = remote_measure(q)
        q.reset()
    assert result == bit

# New and improved method, uses Hadamard gate
def prep_classical_message_h(bit: bool, q: Qubit) -> None:
    if bit:
        q.x()
    q.h()

def remote_measure_h(q: Qubit) -> bool:
    q.h()
    return q.measure()

def send_classical_message_h(device: QuantumDevice, bit: bool) -> None:
    with device.using_qubit() as q:
        prep_classical_message_h(bit, q)
        result = remote_measure_h(q)
        assert result == bit

# Flawed method, using one basis for encrypt and other for decrypt
def send_classical_message_flawed(device: QuantumDevice, bit: bool) -> None:
    with device.using_qubit() as q:
        prep_classical_message(bit, q)
        result = remote_measure_h(q)
        q.reset()
        assert result == bit, 'Input and output differ!'


if __name__ == '__main__':
    # Set up a simulator with a single qubit for key gen
    qrng_sim = SingleQubitSimulator()

    # Generate a classical key bit
    key_bit = int(qrng(qrng_sim))

    # Generate our 'send bit'
    qkd_sim = SingleQubitSimulator()

    # Use our send bit to simulate passing a msg
    with qkd_sim.using_qubit() as q:
        # Sending a message in the original 'on-off' method
        """
        prep_classical_message(key_bit, q)
        remote_measurement = int(remote_measure(q))
        """
        # Sending a message with the Hadamard gate method
        """
        prep_classical_message_h(key_bit, q)
        remote_measurement = int(remote_measure_h(q))
        """
        """
        # Printing info about the test
        print(f'Prepared classical key bit: {key_bit}')
        print(f'Remote measured: {remote_measurement}')
        """
    # Running multiple times to increase odds of getting incorrect results
    for i in range(5):
        send_classical_message_flawed(qrng_sim, 0)
