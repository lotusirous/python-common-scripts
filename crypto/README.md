This directory consists solution for [cryptopal challenges](https://cryptopals.com).
The challenge problems can help you to understanding a basis level of cryptography which can applied in many area in software security. It also gives some examples in this repository for dead-line developer who want to understand quickly crypto with examples.
Practicing crypto exercises can help you to exploit crypto vulnerabilities in software and protocol.
Thus, it improves product security in design and implementation.

```py
import hashlib

def hash_file(loc):
    return hashlib.sha256(open(loc, 'rb').read()).hexdigest()

def hash_str(string):
    return hashlib.sha256(str.encode(msg)).hexdigest()

def hash_byte(b):
    return hashlib.sha256(b).hexdigest()
```