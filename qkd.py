from interface import QuantumDevice, Qubit

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