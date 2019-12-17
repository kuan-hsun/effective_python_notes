## 03 The difference between bytes, str, and unicode
'''
There are two types to represent characters in Python 3
1. bytes: made by binary data (8 bit value)
2. str: made by Unicode

Represent Unicode into binary data, we need to encode, like UTF-8:
Unicode -> encode -> Binary
Binary -> decode -> Unicode

'''
import os

def to_str(bytes_or_str):
    if isinstance(bytes_or_str, bytes):
        value = bytes_or_str.decode('utf-8')
    else:
        value = bytes_or_str
    return value

def to_bytes(str_to_bytes):
    if isinstance(str_to_bytes, str):
        value = str_to_bytes.encode('utf-8')
    else:
        value = str_to_bytes
    return value


## EXAMPLE 1: always return str/bytes
string_str = 'This is a sample string'
print(type(string_str))
print(to_str(string_str))
print(to_bytes(string_str))

string_bytes = b'This is a sample string'
print(type(string_bytes))
print(to_str(string_bytes))
print(to_bytes(string_bytes))


## EXAMPLE 2: file handles
# 'wb' for write binary
# 'rb' for read binary
with open('./temp/random.bin', 'wb') as f:
    f.write(string_bytes)

with open('./temp/random.txt', 'w') as f:
    f.write(string_str)