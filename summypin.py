import pyotp

# Generate a random base32 secret
secret_key = pyotp.random_base32()
print(f"Your Secret Key: {secret_key}")
