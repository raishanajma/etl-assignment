import json  
import csv   
from datetime import datetime  

with open('data.json', 'r') as json_file: 
    data = json.load(json_file) 

csvfiltered = [csvrecord for csvrecord in data if 'Credit Card Number' in csvrecord] 

csvoutput = datetime.now().strftime('%Y%m%d') + '.csv' 

with open(csvoutput, 'w', newline='') as csvfile:  
    columnnames = ['Name', 'Credit Card Number']  
    writer = csv.DictWriter(csvfile, fieldnames = columnnames) 
    writer.writeheader() 
    for csvrecord in csvfiltered: 
        writer.writerow({'Name': csvrecord['Name'], 'creditcard': csvrecord['Credit Card Number']})

print(f'{csvoutput} has been generated.')