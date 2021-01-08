import os
import csv
import pandas


def main():
    fileread = False
    while not fileread:
        try:
            print("===================Load the CSV file===================")
            filename = input("Type in the name of the file along with extension: ")
            f = open(filename)
            print("CSV file loaded")
            fileread = True
        except Exception as e:
            # error loading file
            print("The file cannot be loaded: ", e)

if __name__ == "__main__":
    main()
