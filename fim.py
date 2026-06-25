import hashlib
import time

# 1. Create a dummy sensitive system file
filename = "system_config.txt"
with open(filename, "w") as f:
    f.write("ALLOW_ACCESS = True\nSERVER_IP = 192.168.1.1")
print(f"[+] Step 1: Created secure file '{filename}'")

# 2. Function to calculate the SHA-256 hash (fingerprint) of the file
def calculate_hash(filepath):
    sha256_hash = hashlib.sha256()
    with open(filepath, "rb") as f:
        for byte_block in iter(lambda: f.read(4096), b""):
            sha256_hash.update(byte_block)
    return sha256_hash.hexdigest()

# 3. Get the original baseline hash
baseline_hash = calculate_hash(filename)
print(f"[+] Step 2: Generated secure baseline hash: {baseline_hash}\n")

# 4. Monitor the file and simulate a hacker tampering with it
print("[*] Starting file monitor...")
for i in range(1, 4):
    time.sleep(1) # Wait 1 second
    current_hash = calculate_hash(filename)
    
    if i == 2:
        print("\n[!] WARNING: A simulated hacker is modifying the file right now...")
        with open(filename, "w") as f:
            f.write("ALLOW_ACCESS = False\nSERVER_IP = 192.168.1.1") # Changed 'True' to 'False'
            
    if current_hash != baseline_hash:
        print(f"[🚨 ALERT] CRITICAL: File tampered with at iteration {i}!")
        print(f"    -> Original Hash: {baseline_hash}")
        print(f"    -> New Mismatched Hash: {current_hash}\n")
        break
    else:
        print(f"[✓] Check {i}: File is safe. Hash matches.")
