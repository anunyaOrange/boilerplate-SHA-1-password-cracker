import hashlib

def crack_sha1_hash(hash, use_salts = False):
    passwords = []
    salts = []
    with open('top-10000-passwords.txt', 'r') as file:
        for line in file:
            passwords.append(line.strip())
    with open('known-salts.txt', 'r') as file:
        for line in file:
            salts.append(line.strip())
    return True