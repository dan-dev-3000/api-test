import secrets

def generate_api_key(length=32):
    return secrets.token_hex(length)

print(f"Generated API Key: {generate_api_key()}")