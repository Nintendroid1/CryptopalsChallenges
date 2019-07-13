import unittest

from hex_to_base64 import hexToBase64
from fixed_xor import fixedXOR
from single_byte_xor import singleByteXOR


'''Testing for Crypto Challenges'''


class TestCrypt(unittest.TestCase):
    # Set 1, Challenge 1
    def test_hex_to_base64(self):
        val = "49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d"
        corr = "SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t"

        self.assertEqual(hexToBase64(val), corr)

    # Set 1, Challenge 2
    def test_fixed_xor(self):
        a = "1c0111001f010100061a024b53535009181c"
        b = "686974207468652062756c6c277320657965"
        corr = "746865206b696420646f6e277420706c6179"

        self.assertEqual(fixedXOR(a, b), corr)

    def test_single_byte_xor(self):
        val = "1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736"

        for i in range(0, 255):
            print(singleByteXOR(val, i))

        for j in range(97, 123):
            print(chr(j))


if __name__ == "__main__":
    unittest.main()
