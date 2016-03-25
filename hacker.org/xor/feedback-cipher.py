from xor import *

txt = "aaabbbccc"
k = "#"

for char in txt:
    newchar = xor(char, k, 8)
    print newchar