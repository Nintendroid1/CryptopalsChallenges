"""
    Analyzes the frequency of the plaintext

    https://laconicwolf.com/2018/05/29/cryptopals-challenge-3-single-byte-xor-cipher-in-python/
"""

def frequencyAnalyzer(text):
    # From https://en.wikipedia.org/wiki/Letter_frequency
    # with the exception of ' '
    character_frequencies = {
        'a': .08167, 'b': .01492, 'c': .02782, 'd': .04253,
        'e': .12702, 'f': .02228, 'g': .02015, 'h': .06094,
        'i': .06094, 'j': .00153, 'k': .00772, 'l': .04025,
        'm': .02406, 'n': .06749, 'o': .07507, 'p': .01929,
        'q': .00095, 'r': .05987, 's': .06327, 't': .09056,
        'u': .02758, 'v': .00978, 'w': .02360, 'x': .00150,
        'y': .01974, 'z': .00074, ' ': .13000
    }

    scores = []

    for byte in text.lower():
        # Find character's frequency, if not found return 0
        score = character_frequencies.get(chr(byte), 0)

        scores.append(score)

    return sum(scores)
