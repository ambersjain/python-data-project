import os
import csv
import json
import pandas as pd
from collections import OrderedDict


def convertToJson(data):
    json = data.to_dict(orient='records')
    with open('convertedJson.json', 'w') as f:
        f.write(str(json))
    print ("File is generated and stored in the directory")


def presentDataSummary():
    pass


def sqlInsert():
    pass


def main():
    fileread = False
    while not fileread:
        try:
            print("===================Load the CSV file===================")
            filename = input("Type in the name of the file along with extension: ")
            # f = open(filename)
            # data = list(csv.reader(f))
            data = pd.read_csv(filename)
            print("===================CSV file loaded=========================")
            fileread = True
        except Exception as e:
            # error loading file
            print("The file cannot be loaded: ", e)
        else:
            correct_option_selected = False
            while not correct_option_selected:
                print("1. Convert CSV to JSON")
                print("2. Check Data Summary")
                print("3. Generate a SQL insert statement for all rows in the input")
                option = input("Select 1, 2 or 3 from above: ")
                if option == '1':
                    correct_option_selected = True
                    print("Converting CSV to JSON......")
                    convertToJson(data)
                elif option == '2':
                    correct_option_selected = True
                    print("Presenting data summary......")
                    presentDataSummary()
                elif option == '3':
                    correct_option_selected = True
                    print("Generate a SQL insert statement for all rows in the input......")
                    sqlInsert()
                else:
                    print("Please input a correct integer [1,2 or 3]......")


if __name__ == "__main__":
    main()
