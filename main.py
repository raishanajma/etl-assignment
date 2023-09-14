import csv
import json
from datetime import datetime

filtered_data = [listdata for listdata in data if 'Credit Card' in listdata]

csv_output = datetime.now().strftime('%Y/%m/%d') + '.csv'