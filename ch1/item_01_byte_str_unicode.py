## 03 The difference between bytes, str, and unicode
'''
There are two types to represent characters in Python 3
1. bytes: made by binary data (8 bit value)
2. str: made by Unicode

Represent Unicode into binary data, we need to encode, like UTF-8:
Unicode -> encode -> Binary
Binary -> decode -> Unicode

'''


def to_str(bytes_or_str):
    if isinstance(bytes_or_str, bytes):
        value = bytes_or_str.decode('utf-8')
    else:
        value = bytes_or_str
    return value

if __name__ == '__main__':
    to_str(bytes_or_str)