from zipfile import ZipFile
from pathlib import Path

script_dir = Path(__file__).parent

def attempt_extract(zf_handle, password):
    try:
        zf_handle.extractall(pwd=password.encode())
        return True  # Password found and extraction successful
    except Exception as e:
        # Incorrect password or other error during extraction
        return False

def main():
    print("[+] Beginning bruteforce ")
    zip_file = script_dir / 'enc.zip'
    password_file = script_dir / 'rockyou.txt'
    
    with ZipFile(zip_file) as zf:
        with open(password_file, 'r', errors='ignore') as f:
            passwords = f.readlines()
        
        for password in passwords:
            password = password.strip()  
            
            if attempt_extract(zf, password):
                print(f"[+] Password found: {password}")
                break
            else:
                print(f"[-] Attempting password: {password}")

    print("[+] Password not found in list")

if __name__ == "__main__":
    main()
