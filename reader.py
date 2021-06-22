import csv
import sys
import json

class File:
    def __init__(self):
        self.encoded = []
        return

    def read(self, file):
        with open(file, 'r') as file:
            reader = csv.reader(file)
            for line in reader:
                self.encoded.append(json.dumps(line))
            return True

    def save(self, file):
        with open(file, 'w') as file:
            for line in self.encoded:
                file.write(line)
            return True

fi = File()

while True:
    infile = sys.argv[1]
    outfile = sys.argv[2]
    if not infile:
        print('Error')
    fi.read(infile)
    fi.save(outfile)
    break