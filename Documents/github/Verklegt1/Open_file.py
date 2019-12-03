import csv

class FileWriter:
    def __init__(self):
        self.path='STUDENTDATA/' #laga

    def writeFileWithHeader(self, fileName, header, data):
        path = self.path + fileName
        file_object = open(path, 'a')
        #w ef skrifa eða yfirskrifa
        #r ef lesa skrá
