import csv, sys, json, pickle, os

# file_content.encode("utf-8")
# file_content.decode("utf-8")


class File:
    def __init__(self):
        self.file_content = []

    def read(self, file):
        extension = file.split('.')[-1]
        if extension == 'csv':
            self.read_csv(file)
        elif extension == 'json':
            self.read_json(file)
        elif extension == 'pickle':
            self.read_pickle(file)
        else:
            print('Error')
            return False
        return True

    def read_csv(self, file):
        with open(file, 'r', newline="") as fp:
            reader = csv.reader(fp)
            for line in reader:
                self.file_content.append(line)
            return True

    def read_json(self, file):
        with open(file, 'r') as fp:
            reader = fp.read()
            self.file_content = json.loads(reader)
            return True

    def read_pickle(self, file):
        with open(file, 'rb') as fp:
            reader = fp.read()
            self.file_content = pickle.loads(reader.decode("utf-8"))
            return True

    def change(self, change):
        for parameter in change:
            param_list = parameter.split(",")
            if int(param_list[1])-1 == 0:
                self.file_content[int(param_list[0]) - 1][int(param_list[1]) - 1] = param_list[2]
            else:
                self.file_content[int(param_list[0])-1][int(param_list[1])-1] = "  " + param_list[2]

    def save(self, file):
        extension = file.split('.')[-1]
        if extension == 'csv':
            self.save_csv(file)
        elif extension == 'json':
            self.save_json(file)
        elif extension == 'pickle':
            self.save_pickle(file)
        else:
            print('Error')
            return False
        return True

    def save_csv(self, file):
        with open(file, 'w', newline="") as fp:
            writer = csv.writer(fp)
            for line in self.file_content:
                writer.writerow(line)
            return True

    def save_json(self, file):
        with open(file, 'w') as fp:
            file_content_json = json.dumps(self.file_content)
            fp.write(file_content_json)
        return True

    def save_pickle(self, file):
        with open(file, 'wb') as fp:
            file_content_pickle = pickle.loads(self.file_content)
            fp.write(file_content_pickle)
        return True

    def isfile(self, file):
        if os.path.exists(file):
            return True
        else:
            print('Error')
            path = os.getcwd()
            files = os.system(dir)

fi = File()
infile = sys.argv[1]
outfile = sys.argv[2]
changes = sys.argv[3:]

fi.isfile(infile)
fi.read(infile)
fi.change(changes)
fi.save(outfile)
