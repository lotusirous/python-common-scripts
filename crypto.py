import hashlib

def hash_file(loc):
    return hashlib.sha256(open(loc, 'rb').read()).hexdigest()

def hash_str(string):
    return hashlib.sha256(str.encode(msg)).hexdigest()

def hash_byte(b):
    return hashlib.sha256(b).hexdigest()
