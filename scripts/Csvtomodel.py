import csv
from indiatorlibrary.quickstart.models import Indicator
 with open('indlib8.csv') as f:
    reader = csv.reader(f)
    for row in reader:
        p = Indicator(#Enter the model attribute and row here: like name = row[2]#)             
	arr.append(p)
	p.save()
