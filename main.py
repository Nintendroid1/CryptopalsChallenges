import unittest

from hex_to_base64 import hexToBase64
from fixed_xor import fixedXOR
from single_byte_xor import singleByteXOR
from frequency import frequencyAnalyzer

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
        corr = "Cooking MC's like a pound of bacon"

        self.assertEqual(set1Chal3Solution(val), corr)
    
    def test_detect_single_char_xor(self):
      corr = "Now that the party is jumping\n"
      self.assertEqual(set1Chal4Solution(), corr)


# Iterate through int character values (0-255)


def set1Chal3Solution(val):
    result = ''
    bestScore = 0
    for i in range(0, 255):
        temp = singleByteXOR(val, i)
        tempScore = frequencyAnalyzer(temp)
        if(tempScore > bestScore):
            bestScore = tempScore
            result = temp
    return result.decode()
  
def set1Chal4Solution():
  # with statement will automatically close the file 
  # after the nested block of code
  with open("Data/4.txt", "r") as file: 
    data = file.readlines()
    bestScore = 0
    result = ''
    for line in data: 
      word = line.split() 
      wordStr = ''.join(word)#List -> Str
            
      for i in range(0, 255):
        temp = singleByteXOR(wordStr, i)
        tempScore = frequencyAnalyzer(temp)
        if(tempScore > bestScore):
          bestScore = tempScore
          result = temp
            
  return result.decode()


if __name__ == "__main__":
    unittest.main()
