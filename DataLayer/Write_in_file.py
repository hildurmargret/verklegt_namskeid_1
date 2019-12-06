import csv

class FileWriter:
    def __init__(self):
        self.path='STUDENTDATA/' #laga

    def writeFileWithHeader(self, fileName, header, data):
        path = self.path + fileName
        file_object = open(path, 'a') #w ef skrifa eða yfirskrifa
        writer = csv.writer(file_object)
        writer.writerow(header)
        writer.writerow(data)

    if __name__== "__main__":
        file=FileWriter()
