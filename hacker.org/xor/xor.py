import binascii

# text - hexadecimal
# key  - decimal
def xor_hex(text, key, key_bit_length):

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

def hextobin(h):
    return bin(int(h, 16))[2:].zfill(len(h) * 4)

def dectobin(x):
    return bin(x)[2:]

# hex_byte = "aa", "3f", "d4" etc.
# key = decimal [0, 255]
def xor_1byte(hex_byte, key):
    binary = hextobin(hex_byte)
    binkey = dectobin(key)

    # loop through each bit, comparing text and key values
    binary_text = ""
    for i in range(len(binary)):
        # binary key is 8 bits long
        if binary[i] != binkey[i % 8]:
            binary_text += "1"
        else:
            binary_text += "0"

    # at this point the result is a binary number
    # we need to convert it into a string
    string_blocks = (binary_text[i:i+8] for i in range(0, len(binary_text), 8))
    string = ''.join(chr(int(char, 2)) for char in string_blocks)
    return string