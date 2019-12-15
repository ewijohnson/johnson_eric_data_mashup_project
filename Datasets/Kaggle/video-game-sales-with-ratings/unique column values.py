"""
This script can be adjusted to get the unique column values in any of the columns in the Kaggle dataset.
This script was used to complete my data documentation, in order to see how many unique values are
in each column.
"""

import csv

unique_values = []
missing_values = []

col_num = 2  # Column number, start counting with 1 because this is accounted for

with open('Video_Games_Sales_as_at_22_Dec_2016.csv') as csvfile:
    infile = csv.reader(csvfile)
    for row in infile:
        if row[col_num-1] == '':
            missing_values.append((row[col_num-1]))
        if row[col_num-1] not in unique_values:
            unique_values.append((row[col_num-1]))

        # try:
        #     int(row[col_num-1])
        # except:
        #     unique_values.append((row[col_num - 1]))

    # print(len(unique_values))

    for value in unique_values:
        print('*' + value)

    print(len(unique_values))
