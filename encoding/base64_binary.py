"""
This script convert binary file to base64 text file, then convert back to binary file
author: khant
"""
import base64

filepath = 'infile.tar'
encoded_file = 'encoded.txt'
outfile = 'out.tar'


def encode_to_file(read_file, encoded_file):
    with open(read_file, 'rb') as infile:
        data = infile.read()

    encoded = base64.encodestring(data)
    with open(encoded_file, 'w') as f:
        f.write(encoded)


def decode_from_file(filepath, outfile):
    with open(filepath) as f:
        encoded = f.read()
    decoded_str = base64.decodestring(encoded)
    print(type(decoded_str))
    with open(outfile, 'wb') as f:
        f.write(decoded_str)


def main():
    encode_to_file(filepath, encoded_file)
    decode_from_file(encoded_file, outfile)


if __name__ == '__main__':
    main()
