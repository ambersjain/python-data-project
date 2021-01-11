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


def presentDataSummary(data):
    # Get % of people with Google Play and iOS
    # Get % of people with phone brand
    # Get % of device cat
    os_type = data['sku'].value_counts(normalize=True) * 100
    device_model_counts_top5 = data['device_model_name'].value_counts()[0:5]
    install_source_top5 = data['install_source'].value_counts()[0:5]
    geo_region_top5 = data['geo_region'].value_counts()[0:5]
    print ("========================DATA SUMMARY============================")
    print ("=> The OS type percentage for the users")
    print (os_type)
    print ("================================================================")
    print ("=> Top 5 device models used for the app")
    print (device_model_counts_top5)
    print ("================================================================")
    print ("=> Top 5 install sources used for the app")
    print (install_source_top5)
    print ("================================================================")
    print ("=> Where do the users install the app from? (Top 5)")
    print (geo_region_top5)
    print ("========================DATA SUMMARY END==========================")

def sqlInsert(SOURCE):
    sql_texts = []
    for index, row in SOURCE.iterrows():
        sql_texts.append(
            'INSERT INTO ' + 'table' + '(' + str(', '.join(SOURCE.columns)) + ') VALUES ' + str(tuple(row.values)))
    print('\n\n'.join(sql_texts))

def main():
    fileread = False
    while not fileread:
        try:
            print("===================Load the CSV file===================")
            filename = input("Type in the name of the file along with extension: ")
            data = pd.read_csv(filename)
            print("===================CSV file loaded=========================")
            fileread = True
        except Exception as e:
            # error loading file
            print("The file cannot be loaded: ", e)
        else:
            correct_option_selected = False
            while not correct_option_selected:
                print("===================MENU========================")
                print("1. Convert CSV to JSON")
                print("2. Check Data Summary")
                print("3. Generat a SQL insert statement for all rows in the input")
                print("4. Exit")
                option = input("Choose 1, 2, 3 or 4 from above: ")
                if option == '1':
                    print("Converting CSV to JSON......")
                    convertToJson(data)
                elif option == '2':
                    print("Presenting data summary......")
                    presentDataSummary(data)
                elif option == '3':
                    print("Generating a SQL insert statement for all rows in the input......Please allow 5 seconds")
                    sqlInsert(data)
                elif option == '4':
                    correct_option_selected = True
                    print("Thanks for using the app.")
                else:
                    print("Please input a correct integer [1,2 or 3]......")


if __name__ == "__main__":
    main()
