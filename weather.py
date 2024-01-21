import csv

csv_fileread='weather.csv'

with open(csv_fileread, 'r') as csvfileinput:
    # Create a CSV reader object
    csv_reader = csv.reader(csvfileinput)

    for line in csv_fileread.readlines():
        array = line.split(',')
        first_item = array[0]
    num_columns = len(array)
    csv_fileread.seek(0)

    included_cols=[1, 34, 42]


    with open('weatherResult.csv', 'w') as output:
        csv_writer= csv.writer(output)
        #included_cols=[1, 34,42]
        # for line in csv_reader:
        #    csv_writer.writerow(line)
        #
        
        for row in csv_reader:
            content = list(row[i] for i in included_cols)
            csv_writer.writerow(line)







