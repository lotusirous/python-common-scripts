import hashlib

def hash_file(loc):
    return hashlib.sha256(open(loc, 'rb').read()).hexdigest()
