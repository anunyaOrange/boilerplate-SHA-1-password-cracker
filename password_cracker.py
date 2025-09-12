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
        hex = hashlib.sha1(pwd.encode('utf-8')).hexdigest()
        if hex == hash:
            print(pwd)
    return True

print('xxxxxxxxxxxxxxxxxxxxxxx')
crack_sha1_hash('b305921a3723cd5d70a375cd21a61e60aabb84ec')
