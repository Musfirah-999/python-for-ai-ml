from cryptography.fernet import Fernet
import hashlib

def write_key(master_password):
    key = Fernet.generate_key()
    key_filename = f"key_{hashlib.sha256(master_password.encode()).hexdigest()[:16]}.key"
    with open(key_filename, "wb") as key_file:
        key_file.write(key) 
        
def load_key(master_password):
    key_filename = f"key_{hashlib.sha256(master_password.encode()).hexdigest()[:16]}.key"
    try:
        file = open(key_filename, "rb")
        key = file.read()
        file.close()
        return key, key_filename
    except FileNotFoundError:
        print("No passwords stored for this master password.")
        return None, key_filename  # Return None and the filename

def get_master_key():
    master_pwd = input("What is the master password? ")
    key_data = load_key(master_pwd)
    if key_data[0] is None:
        create_new = input("No passwords found for this master password. Create new password vault? (yes/no): ").lower()
        if create_new == "yes":
            write_key(master_pwd)
            key_data = load_key(master_pwd)
            if key_data[0] is None:
                print("Error creating vault. Please try again.")
                return None, None
            print("New vault created successfully!")
            return key_data[0], master_pwd
        else:
            return None, None
    return key_data[0], master_pwd

def view(fer, master_pwd_hash):
    filename = f"passwords_{master_pwd_hash}.txt"
    try:
        with open(filename, 'r') as f:
            content = f.read()
            if not content.strip():
                print("No passwords stored yet.")
                return
                
            f.seek(0)
            for line in f.readlines():
                data = line.rstrip()
                if "|" not in data:
                    continue
                user, passw = data.split("|")
                try:
                    decrypted = fer.decrypt(passw.encode()).decode()
                    print("User:", user, "| Password:", decrypted)
                except Exception as e:
                    print(f"Error decrypting password for {user}: {e}")

    except FileNotFoundError:
        print("No passwords stored yet.")

def add(fer, master_pwd_hash):
    name = input("Account name: ")
    pwd = input("Password: ")
    
    filename = f"passwords_{master_pwd_hash}.txt"
    with open(filename, 'a') as f:
        f.write(name + "|" + fer.encrypt(pwd.encode()).decode() + "\n")
    print("Password added successfully!")

def main():
    key, master_pwd = get_master_key()
    if key is None:
        print("Access denied or vault creation cancelled.")
        return
    
    fer = Fernet(key)
    master_pwd_hash = hashlib.sha256(master_pwd.encode()).hexdigest()[:16]
    
    while True:
        mode = input("\nWould you like to add a new password or view existing ones (view, add) or press q to quit? ").lower()
        if mode == "q":
            break
        if mode == "view":
            view(fer, master_pwd_hash)
        elif mode == "add":
            add(fer, master_pwd_hash)
        else:
            print("Invalid mode.")
            continue

if __name__ == "__main__":
    main()