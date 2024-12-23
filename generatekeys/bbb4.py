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

if __name__ == "__main__":
    # Example usage: generate a 256-bit quantum key using BB84
    key_length_in_bits = 256
    quantum_key = simulate_bb84_protocol(key_length_in_bits)

    print(f"Generated quantum key (BB84): {quantum_key}")
