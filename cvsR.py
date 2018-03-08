
#Table creator, Table = companies, db  = Inc5000

import csv

with open('inc5000-2017.csv') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')

    print('INSERT INTO companies (rank, company_name, headcount, industry) VALUES')

    for row in readCSV:

            print('(' + row[1] + ',\'' + row[2] + '\',' + row[11] + ',\'' + row[12]+ '\'),')
