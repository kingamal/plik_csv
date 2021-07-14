import csv
import sys
import json
import pickle
import os

# file_content.encode("utf-8")
# file_content.decode("utf-8")


class File:
    def __init__(self):
        self.file_content = []

    def change(self, change):
        for parameter in change:
            param_list = parameter.split(",")
            rows = len(self.file_content)
            columns = len(param_list[0:])
            if int(param_list[0]) - 1 <= rows and int(param_list[1]) - 1 <= columns:
                if int(param_list[1]) - 1 == 0:
                    self.file_content[int(param_list[0]) - 1][int(param_list[1]) - 1] = param_list[2]
                else:
                    self.file_content[int(param_list[0]) - 1][int(param_list[1]) - 1] = "  " + param_list[2]
            else:
                print('Zła kolumna albo wiersz!')

    def create(src, dst):
        src_cls = ReadCSV
        if src == "json":
            src_cls = ReadJSON
        if src == "pickle":
            src_cls = ReadPickle
        dst_cls = SaveCSV
        if dst == "json":
            dst_cls = SaveJSON
        if dst == "pickle":
            dst_cls = SavePickle

        class Parser(src_cls, dst_cls):
            pass

        return Parser

    def factory(file_in, file_out):
        extension_in = file_in.split('.')[-1]
        extension_out = file_out.split('.')[-1]
        return File.create(extension_in, extension_out)

    def isfile(self, file):
        if os.path.exists(file):
            return True
        else:
            print('Error - Nie ma takiego pliku wejściowego!')
            catalogs = list(os.listdir())
            print('Pliki, które znajdują się w tym katalogu to:')
            for cat in catalogs:
                print(cat)
            return False


class ReadCSV(File):
        def read(self, file):
            try:
                with open(file, 'r', newline="") as fp:
                    reader = csv.reader(fp)
                    for line in reader:
                        self.file_content.append(line)
                        print(line)
                    return True
            except FileNotFoundError:
                self.isfile(file)


class SaveCSV(File):
    def save(self, file):
        with open(file, 'w', newline="") as fp:
            writer = csv.writer(fp)
            for line in self.file_content:
                writer.writerow(line)
            return True

class ReadJSON(File):
    def read(self, file):
        try:
            with open(file, 'r') as fp:
                reader = fp.read()
                self.file_content = json.loads(reader)

                for line in self.file_content:
                    print(line)
                return True
        except FileNotFoundError:
            self.isfile(file)


class SaveJSON(File):
    def save(self, file):
        with open(file, 'w') as fp:
            file_content_json = json.dumps(self.file_content)
            fp.write(file_content_json)
        return True


class ReadPickle(File):
    def read(self, file):
        try:
            with open(file, 'rb') as fp:
                reader = fp.read()
                self.file_content = pickle.loads(reader)

                for line in self.file_content:
                    print(line)
                return True
        except FileNotFoundError:
            self.isfile(file)


class SavePickle(File):
    def save(self, file):
        with open(file, 'wb') as fp:
            file_content_pickle = pickle.dumps(self.file_content)
            fp.write(file_content_pickle)
        return True


infile = sys.argv[1]
outfile = sys.argv[2]
changes = sys.argv[3:]

fi = File.factory(infile, outfile)()
fi.read(infile)
fi.change(changes)
fi.save(outfile)


