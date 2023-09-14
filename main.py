import json
import csv
from datetime import datetime

with open('data.json', 'r') as json_file: 
    data = json.load(json_file)

filtered_csv = [listdata for listdata in data if 'Credit Card Number' in listdata]

csv_output = datetime.now().strftime('%Y/%m/%d') + '.csv'

with open(csv_output, 'w', newline='') as csv_list:
    column_names = ['Name', 'Credit Card Number']
    writer = csv.DictWriter(csv_list, column_names = column_names)
    writer.writeheader()
    for listdata in filtered_csv:
        writer.writerow({'name': record['Name'], 'creditcard': record['Credit Card Number']})

print('{csv_output} has been generated.')