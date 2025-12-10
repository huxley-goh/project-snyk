# Vulnerable: Hardcoded password
PASSWORD = "mysecretpassword123"

def authenticate(provided_password):
    if provided_password == PASSWORD:
        print("Authentication successful!")
    else:
        print("Authentication failed.")

authenticate("wrong_password")