
#Table creator, Table = companies, db  = Inc5000

import csv

with open('inc5000.csv') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')

    for row in readCSV:
            print('INSERT INTO companies (rank, company_name, headcount, industry)')
            print('VALUES(\'', row[1] + '\',\'' + row[2] + '\',\'' + row[11] + '\',\'' + row[12]+ '\');')
