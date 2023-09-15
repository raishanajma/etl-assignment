import csv  
import json   
from datetime import datetime  

with open('data.json', 'r') as json_file: 
    record = json.load(json_file) 

csvfiltered = [datacsv for datacsv in record if 'Credit Card Number' in datacsv] 

csvoutput = datetime.now().strftime('%Y/%m/%d') + '.csv' 

with open(csvoutput, 'w', newline='') as csvfile:  
    columnnames = ['Name', 'Credit Card Number']  
    writer = csv.DictWriter(csvfile, columnnames = columnnames) 
    writer.writeheader() 
    for datacsv in csvfiltered: 
        writer.writerow({'Name': record['Name'], 'creditcard': record['Credit Card Number']})

print(f'{csvoutput} has been generated.')