'''
Single byte xor

https://laconicwolf.com/2018/05/29/cryptopals-challenge-3-single-byte-xor-cipher-in-python/

'''


def singleByteXOR(byteArr, singleChar):
    # Bytes literal
    result = b''

    # Iterate every byte and do a XOR
    for byte in byteArr:
        result += bytes([byte ^ singleChar])
    return result
