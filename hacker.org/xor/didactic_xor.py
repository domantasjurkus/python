from xor import *

chal1 = "3d2e212b20226f3c2a2a2b"
chal2 = "948881859781c4979186898d90c4c68c85878f85808b8b808881c6c4828b96c4908c8d97c4878c858888818a8381"
chal3 = "31cf55aa0c91fb6fcb33f34793fe00c72ebc4c88fd57dc6ba71e71b759d83588"

# Challenge 2
for i in range(1, 256):
    print i, xor_hex(chal2, i, 8)



# Challenge 3
# b = [0, 255]
# x = [0, 255]

def xor_chal3(text, key, key_bit_length):

    # transform the string into a binary representation
    binary = ""
    for i in range(0, len(text), 2):
        char = text[i:i+2]
        binary += hextobin(char)

    # transform the key into a binary representation    
    binkey = dectobin(key)
    while len(binkey) < key_bit_length:
        binkey = "0" + binkey

    # loop through each bit, comparing text and key values
    binary_text = ""
    for i in range(len(binary)):
        # xor
        if binary[i] != binkey[i % key_bit_length]:
            binary_text += "1"
        else:
            binary_text += "0"
            
    # at this point the result is a binary number
    # we need to convert it into a string
    string_blocks = (binary_text[i:i+8] for i in range(0, len(binary_text), 8))
    string = ''.join(chr(int(char, 2)) for char in string_blocks)
    return string