import pandas as pd
from matplotlib import pyplot as plt
import xlrd 

loc = ("global_terrorism_database.xlsx")   
wb = xlrd.open_workbook(loc) 
sheet = wb.sheet_by_index(0)  
D = {}

for i in range(sheet.nrows - 1): 
	region = sheet.cell_value(i+1,10)
	if region=="North America":
		decade = int(sheet.cell_value(i+1,1))
		decade = decade - decade%10
		decade = str(decade)
		if decade in D:
			D[decade]+=1
		else:
			D[decade]=1

print(D)
plt.bar(range(len(D)), list(D.values()), align='center')
plt.xticks(range(len(D)), list(D.keys()))
plt.xlabel('Decade')
plt.ylabel('Frequency of crime in North America')
plt.show()