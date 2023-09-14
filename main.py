import csv
import json
from datetime import datetime

with open('data.json', 'r') as json_file: 
    record = json.load(json_file)

filtered_csv = [csvrecord for csvrecord in record if 'Credit Card Number' in csvrecord]

csv_output = datetime.now().strftime('%Y/%m/%d') + '.csv'

with open(csv_output, 'w', newline='') as csv_list:
    column_names = ['Name', 'Credit Card Number']
    writer = csv.DictWriter(csv_list, column_names = column_names)
    writer.writeheader()
    for csvrecord in filtered_csv:
        writer.writerow({'name': csvrecord['Name'], 'creditcard': csvrecord['Credit Card Number']})

print('{csv_output} has been generated.')