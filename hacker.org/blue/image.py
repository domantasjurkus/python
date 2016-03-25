from PIL import Image

img = Image.open("green.png")

width = 84
height = 1
pixelMap = img.load()

for y in xrange(height):
    str = ""
    for x in xrange(width):
        pixel = pixelMap[x, y][1]
        str += chr(pixel)
    print str
