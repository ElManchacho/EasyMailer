import csv
import pandas as pd
import json


def loadInfos():

    json_file = open("../data/env.json")
    variables = json.load(json_file)
    json_file.close()
    
    """
    excelPath = "../data/MailList.xlsx"

    csvPath = "../data/MailList.csv"

    read_excel_file = pd.read_excel(excelPath)

    read_excel_file.to_csv(csvPath, index=None, header=True)

    headers = []

    rows = []

    indexes = []

    index = 0

    file = open(csvPath)
    csvreader=csv.reader(file)
    headers = next(csvreader)
    for row in csvreader:
        indexes.append(index)
        index=index+1
        rows.append(row)

    df1 = pd.DataFrame(rows,
                   index=indexes,
                   columns=headers)
    """
    df1 = []

    return [variables,df1]
