import csv

if __name__ == '__main__':
    column_name_list = ['id', 'fileName', 'sampleSize', 'eliteSize', 'smoothParameter', 'iterationNumber',
                            'consumesTimes', 'optimalValue']
    testdata=[1,1,1,1,1,1,1,1]
    with open('1.csv','a+',newline='') as f:
        f_csv = csv.writer(f)
        for i in range(0,5):
            f_csv.writerow(testdata)