
import xlrd 
import matplotlib.pyplot as plt

loc = ("baltimore_crimes.xlsx")   
wb = xlrd.open_workbook(loc) 
sheet = wb.sheet_by_index(0)  
D = {"CENTRAL":0,"WESTERN":0,"NORTHERN":0,"SOUTHERN":0,"EASTERN":0,"NORTHEASTERN":0,"NORTHWESTERN" :0, "SOUTHEASTERN":0,"SOUTHWESTERN":0}

for i in range(sheet.nrows - 1): 
	district = sheet.cell_value(i+1,7)
	D[district]+=1

print(D)
plt.bar(range(len(D)), list(D.values()), align='center')
plt.xticks(range(len(D)), list(D.keys()))
plt.xlabel('Districts')
plt.ylabel('Frequency of crime')
plt.show()