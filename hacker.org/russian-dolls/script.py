import gzip
import shutil

import os 
os.system("calc")

def extract_from_to(from_name, to_name):

    try:
        with gzip.open(from_name, 'r') as infile:
            with gzip.open(to_name, 'w') as outfile:

                # Generate the output file
                for line in infile:
                    print str(line)
                    outfile.write(line)

                infile.close()
                outfile.close()  

                # Move the old file away
                # shutil.move(from_name, "del\\" + from_name)

    except:
        raise 

'''
i = 1
while True:
    try:
        extract_from_to('out' + str(i), 'out' + str(i+1))
        print 'out' + str(i), 'out' + str(i+1)
        i += 1
    except:
        print "Whoa, can't extract anymore"
        break
'''

extract_from_to('doll', 'out')