import csv

if __name__ == '__main__':
    column_name_list = ['id', 'fileName', 'sampleSize', 'eliteSize', 'smoothParameter', 'iterationNumber',
                        'consumesTimes', 'optimalValue']
    testData = [1, 1, 1, 1, 1, 1, 1, 1]
    with open('.\\out\\appendicitis.csv', 'a+', newline='') as f:
        f_csv = csv.writer(f)
        f_csv.writerow(column_name_list)
