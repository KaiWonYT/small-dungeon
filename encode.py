from zlib import decompress, compress
from base64 import b64decode, b64encode

# Decode: zlib decompress, then base64 decode
def decode_spec(data):
    return decompress(b64decode(data)).decode("utf-8")


# Encode: base64 encode, then zlib compress
def encode_spec(data):
    return b64encode(compress(data.encode("utf-8")))

def test():
    from random import randint
    data = str(randint(0,255))
    print(decode_spec(encode_spec(data)) == data)