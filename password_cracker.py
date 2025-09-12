import hashlib

def crack_sha1_hash(hash, use_salts = False):
    passwords = []
    salts = []
    with open('top-10000-passwords.txt', 'r') as file:
        for line in file:
            passwords.append(line.strip())
    with open('known-salts.txt', 'r') as file:
        for line in file:
            salts.append(line.strip().encode('utf-8'))

    for pwd in passwords:
        if use_salts:
            for salt in salts:
                hex = hashlib.sha1(salt + pwd.encode('utf-8') + salt).hexdigest()
                if hex == hash:
                    print('salts', pwd)                
        else:
            hex = hashlib.sha1(pwd.encode('utf-8')).hexdigest()
            if hex == hash:
                print(pwd)
    return True

print('xxxxxxxxxxxxxxxxxxxxxxx')
# crack_sha1_hash('b305921a3723cd5d70a375cd21a61e60aabb84ec')
crack_sha1_hash('53d8b3dc9d39f0184144674e310185e41a87ffd5', True)
