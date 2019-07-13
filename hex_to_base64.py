'''
Encode hex string to base64 string
https://www.geeksforgeeks.org/encode-ascii-string-base-64-format/

Library equivalent:
base64.b64encode(str)
'''


def hexToBase64(ct: str):
    # Convert hex string to bytes object then decode to ascii
    ctAscii = bytearray.fromhex(ct).decode()

    alphabet = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "a", "b", "c", "d", "e",
                "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "+", "/"]
    result = []
    padding = 0

    # Loop through characters 3 at a time and store in string
    ctLen = len(ctAscii)
    for i in range(0, ctLen, 3):
        binData = 0
        cnt = 0
        numBits = 0

        j = i
        while(j < ctLen and j <= i+2):
            binData = binData << 8
            binData = binData | ord(ctAscii[j])
            cnt += 1
            j += 1

        numBits = cnt*8

        # How much "=" to append
        padding = numBits % 3

        # Extracts all bits 6 at a time
        while(numBits != 0):
            # Retrieve the value of each block
            if(numBits >= 6):
                temp = numBits - 6

                # 63 => 111111
                index = (binData >> temp) & 63
                numBits -= 6
            else:
                temp = 6 - numBits

                # Append with 0 if less than 6
                index = (binData << temp) & 63
                numBits = 0
            result.append(alphabet[index])
    # Padding
    for i in range(1, padding+1):
        result.append('=')

    return ''.join(result)
