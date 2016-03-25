f = open("3280.txt", "r")
line = "blah"

words = {}

while True:
    line = f.readline();

    list = line[:-1].split();
    for word in list:
        if len(word) != 9:
            continue
        if words.has_key(word):
            words[word] += 1
        else:
            words[word] = 1
            
    if line == "":
        break

f.close()

for word in words:
    print word, words[word]
