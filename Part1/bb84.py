from interface import QuantumDevice, Qubit
from simulator import SingleQubitSimulator
from typing import List

# Sample random bit for message passing
def sample_random_bit(device: QuantumDevice) -> bool:
    with device.using_qubit() as q:
        q.h()
        result = q.measure()
        q.reset()
    return result

# Prep msg encoded with a key bit in random basis
def prep_message_qbit(message: bool, basis: bool, q: Qubit) -> None:
    if message:
        q.x()
    if basis:
        q.h()

# Measure the msg qubit and reset for re-use
def measure_message_qubit(basis: bool, q: Qubit) -> bool:
    if basis:
        q.h()
    result = q.measure()
    q.reset()
    return result

# Define helper function for binary -> hex
def convert_to_hex(bits: List[bool]) -> str:
    return hex(int(''.join(["1" if bit else "0" for bit in bits]), 2))

# Sending a single bit
def send_single_bit_bb84(local_device: QuantumDevice, remote_device: QuantumDevice) -> tuple:
    # Get random bit for local msg and basis
    [local_msg, local_basis] = [sample_random_bit(local_device), sample_random_bit(local_device)]
    # Get random bit for local basis
    remote_basis = sample_random_bit(remote_device)

    with local_device.using_qubit() as q:
        prep_message_qbit(local_msg, local_basis, q)
        # "Send" Qubit
        remote_result = measure_message_qubit(remote_basis, q)

    return ((local_msg, local_basis), (remote_result, remote_basis))

# Sending multiple bits to make a full key
def simulate_bb84(num_bits: int) -> tuple:
    # Define quantum devices
    local_device = SingleQubitSimulator()
    remote_device = SingleQubitSimulator()

    # Set up an empty key and counter to track iterations
    key = []
    iterations = 0

    while len(key) < num_bits:
        iterations += 1
        # Generate local and remote info
        ((local_msg, local_basis), (remote_result, remote_basis)) = send_single_bit_bb84(local_device, remote_device)
        # If bases match, we should add the message to the key so long as the msg and result match, too
        if local_basis == remote_basis:
            assert local_msg == remote_result
            key.append(local_msg)

    print(f'Took {iterations} iterations to create key of length {num_bits}.')

    return key

# Create function for one time padding with key
def one_time_pad(msg: List[bool], key: List[bool]) -> List[bool]:
    return [msg_bit ^ key_bit for (msg_bit, key_bit) in zip(msg, key)]


if __name__ == '__main__':
    # Define local and remote quantum devices
    #local_device = SingleQubitSimulator()
    #remote_device = SingleQubitSimulator()

    # Send a single qubit
    #print(send_single_bit_bb84(local_device, remote_device))
    
    # Simulate bb84 with an 8-bit key
    #simulate_bb84(8)

    print("\nRunning bb84 message enc/dec sim\n")
    print("Creating 96 bit key")
    key = simulate_bb84(96)
    print(f"Created key: {convert_to_hex(key)}")
    message = [
1, 1, 0, 1, 1, 0, 0, 0,
0, 0, 1, 1, 1, 1, 0, 1,
1, 1, 0, 1, 1, 1, 0, 0,
1, 0, 0, 1, 0, 1, 1, 0,
1, 1, 0, 1, 1, 0, 0, 0,
0, 0, 1, 1, 1, 1, 0, 1,
1, 1, 0, 1, 1, 1, 0, 0,
0, 0, 0, 0, 1, 1, 0, 1,
1, 1, 0, 1, 1, 0, 0, 0,
0, 0, 1, 1, 1, 1, 0, 1,
1, 1, 0, 1, 1, 1, 0, 0,
1, 0, 1, 1, 1, 0, 1, 1
]
    print(f"\nUsing key to send message: {convert_to_hex(message)}")
    encrypted_msg = one_time_pad(message, key)
    print(f"Decrypting message: {convert_to_hex(encrypted_msg)}")
    decrypted_msg = one_time_pad(encrypted_msg, key)
    print(f"Decrypted message is: {convert_to_hex(decrypted_msg)}")
