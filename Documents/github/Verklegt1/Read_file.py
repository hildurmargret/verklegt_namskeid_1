import csv

def read_file(file_name, row1_name, row2_name):
    row1_name_string = string(row1_name)
    row2_name_string = string(row1_name)
    filename = string(file_name) + ".csv"

    with open(filename, newline = '') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            print(row[row1_name_string], row[row2_name_string])
    
