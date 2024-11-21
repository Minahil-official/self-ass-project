import hashlib
def password():
   while True:
        hash_passwords = {}
        # Input website and password
        website = input("Enter website name (or type 'exit' to stop): ")
        if website.lower() == 'exit':  # Exit condition
            break

        password = input("Enter your password: ")

        # Hash the password
        hashed_values = hashlib.sha256(password.encode()).hexdigest()

        # Store the website and hashed password
        hash_passwords[website] = hashed_values

        pas = password.encode()
        hash_passwords[website] = pas
        my_hash = hashlib.sha256(pas).hexdigest()
        print(f"the hash of password is {my_hash}")
password()