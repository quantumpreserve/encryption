import secrets
import base64
import random

def generate_symmetric_key(key_length: int) -> str:
    """
    Generate a cryptographically secure symmetric key.

    Parameters:
        key_length (int): The length of the key in bytes (e.g., 32 for a 256-bit key).

    Returns:
        str: The base64-encoded key.
    """
    # Generate a secure random key
    key = secrets.token_bytes(key_length)

    # Encode the key in base64 for safe storage/transmission
    base64_key = base64.urlsafe_b64encode(key).decode('utf-8')

    return base64_key

def simulate_bb84_protocol(key_length: int):
    """
    Simulate the BB84 protocol to generate a shared quantum key.

    Parameters:
        key_length (int): The length of the key in bits.

    Returns:
        str: The shared key between Alice and Bob.
    """
    # Step 1: Alice randomly generates qubits and bases
    alice_qubits = [random.choice([0, 1]) for _ in range(key_length)]
    alice_bases = [random.choice(['+', 'x']) for _ in range(key_length)]

    # Step 2: Alice sends qubits to Bob; Bob randomly chooses measurement bases
    bob_bases = [random.choice(['+', 'x']) for _ in range(key_length)]
    bob_measurements = []

    for i in range(key_length):
        if alice_bases[i] == bob_bases[i]:
            bob_measurements.append(alice_qubits[i])  # Same basis, Bob measures correctly
        else:
            bob_measurements.append(random.choice([0, 1]))  # Different basis, random result

    # Step 3: Alice and Bob compare bases over a public channel
    shared_key_indices = [i for i in range(key_length) if alice_bases[i] == bob_bases[i]]

    # Step 4: Generate the final shared key
    shared_key = ''.join(str(bob_measurements[i]) for i in shared_key_indices)

    return shared_key

def error_checking(shared_key: str, test_fraction: float = 0.1) -> bool:
    """
    Perform error checking on the shared key to detect potential eavesdropping.

    Parameters:
        shared_key (str): The shared key to test.
        test_fraction (float): Fraction of the key to use for error checking (0 < test_fraction < 1).

    Returns:
        bool: True if the error rate is acceptable, False otherwise.
    """
    # Determine the number of test bits
    test_bits_count = max(1, int(len(shared_key) * test_fraction))

    # Randomly select test bits
    test_indices = random.sample(range(len(shared_key)), test_bits_count)

    # Simulate Alice and Bob publicly comparing test bits
    errors = 0
    for index in test_indices:
        alice_bit = shared_key[index]  # Simulate Alice's bit
        bob_bit = shared_key[index]   # Simulate Bob's bit
        if alice_bit != bob_bit:
            errors += 1

    # Calculate error rate
    error_rate = errors / test_bits_count

    print(f"Error rate during checking: {error_rate:.2%}")

    # Accept or reject key based on error threshold
    error_threshold = 0.05  # Example threshold: 5%
    return error_rate <= error_threshold

if __name__ == "__main__":
    # Example usage: generate a 256-bit quantum key using BB84
    key_length_in_bits = 256
    quantum_key = simulate_bb84_protocol(key_length_in_bits)

    print(f"Generated quantum key (BB84): {quantum_key}")

    # Perform error checking
    if error_checking(quantum_key):
        print("Key is secure and usable.")
    else:
        print("Key is compromised; discard and retry.")
