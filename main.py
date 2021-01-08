import os
import csv

def main():
    try:
        print("===================Load the CSV file===================")
        filename = input("Type in the name of the file along with extension: ")
        f = open(filename)
        print("CSV file loaded")
    except Exception as e:
        # error loading file
        print("The file cannot be loaded: ", e)
        exit()

if __name__ == "__main__":
    main()
