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

    for pwd in passwords:
        if use_salts:
            for salt in salts:
                hexPrepended = hashlib.sha1((salt + pwd).encode('utf-8')).hexdigest()
                hexAppended = hashlib.sha1((pwd + salt).encode('utf-8')).hexdigest()
                if hexPrepended == hash or hexAppended == hash:
                    return pwd
        else:
            hex = hashlib.sha1(pwd.encode('utf-8')).hexdigest()
            if hex == hash:
                return pwd
    return "PASSWORD NOT IN DATABASE"

