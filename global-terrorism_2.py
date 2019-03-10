import pandas as pd
from matplotlib import pyplot as plt
import xlrd 

loc = ("global_terrorism_database.xlsx")   
wb = xlrd.open_workbook(loc) 
sheet = wb.sheet_by_index(0)  
D = {}
C = {}

for i in range(sheet.nrows - 1): 
	year = sheet.cell_value(i+1,1)
	year=int(year)
	region = sheet.cell_value(i+1,10)
	decade = int(sheet.cell_value(i+1,1))
	#decade = decade - decade%10
	decade = str(decade)
	if year==2014:
		continent = sheet.cell_value(i+1,10)
		if continent in C:
			C[continent]+=1
		else:
			C[continent]=1
	if decade in D:
		D[decade]+=1
	else:
		D[decade]=1

print(D)
for i in D:
	plt.plot(i, D[i], 'ro')
#plt.bar(range(len(D)), list(D.values()), align='center')
#plt.xticks(range(len(D)), list(D.keys()))
plt.xlabel('Year')
plt.xticks(rotation=90)
plt.ylabel('Frequency of crime (Globally)')
plt.show()

print(C)
plt.bar(range(len(C)), list(C.values()), align='center')
plt.xticks(range(len(C)), list(C.keys()))
plt.xlabel('Continent')
plt.ylabel('Frequency of crime in the continent')
plt.xticks(rotation=90)
plt.show()