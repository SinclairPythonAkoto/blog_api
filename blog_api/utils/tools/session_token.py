import secrets


def generate_session_token() -> str:
    """"Creates a random text string in hexidecimal."""
    return secrets.token_hex(16)