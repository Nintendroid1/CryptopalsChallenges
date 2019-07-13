'''
XOR of 2 hex strings
https://stackoverflow.com/questions/14526231/python-xor-hex-strings

a|b|a+b
0|0|0
0|1|1
1|0|1
1|1|0

'''


def fixedXOR(a, b):
    # Convert to integer using base 16 and bitwise XOR
    result = int(a, 16) ^ int(b, 16)

    # Format to hex
    return '{:x}'.format(result)
