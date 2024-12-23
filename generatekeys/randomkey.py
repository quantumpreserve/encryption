import secrets
import base64

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

if __name__ == "__main__":
    # Example usage: generate a 256-bit key (32 bytes)
    key_length_in_bytes = 32  # 256 bits
    symmetric_key = generate_symmetric_key(key_length_in_bytes)

    print(f"Generated symmetric key: {symmetric_key}")
