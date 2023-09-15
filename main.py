import json  
import csv   
from datetime import datetime  

with open('data.json', 'r') as json_file: 
    data = json.load(json_file) 

csvfiltered = [csvrecord for csvrecord in data if 'creditcard' in csvrecord] 

csvoutput = datetime.now().strftime('%Y%m%d') + '.csv' 

with open(csvoutput, 'w', newline='') as csvfile:
    columnnames = ['Name', 'Credit Card Number']  
    writer = csv.DictWriter(csvfile, fieldnames = columnnames) 
    writer.writeheader() 
    for csvrecord in csvfiltered: 
        writer.writerow({'Name': csvrecord['name'], 'Credit Card Number': csvrecord['creditcard']})

print(f'{csvoutput} has been generated.')