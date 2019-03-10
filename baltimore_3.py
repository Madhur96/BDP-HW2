import datetime
import xlrd 
import matplotlib.pyplot as plt

loc = ("baltimore_crimes.xlsx")   
wb = xlrd.open_workbook(loc) 
sheet = wb.sheet_by_index(0)  
D = {"Monday":0,"Tuesday":0,"Wednesday":0,"Thursday":0,"Friday":0,"Saturday":0,"Sunday" :0}
T = {}
for i in range(24):
	i=str(i)
	T[i]=0

for k in range(sheet.nrows - 1): 
	y, m, d, h, i, s = xlrd.xldate_as_tuple(sheet.cell_value(k+1,0), wb.datemode)
	dayofweek = datetime.date(y, m, d).strftime("%A")
	D[dayofweek]+=1
	y, m, d, h2, i, s = xlrd.xldate_as_tuple(sheet.cell_value(k+1,1), wb.datemode)
	t = str(h2)
	#print(t)
	T[t]+=1

print(D)
plt.bar(range(len(D)), list(D.values()), align='center')
plt.xticks(range(len(D)), list(D.keys()))
plt.xlabel('Day of the week')
plt.ylabel('Frequency of crime')
plt.xticks(rotation=90)
plt.show()

print(T)
plt.bar(range(len(T)), list(T.values()), align='center')
plt.xticks(range(len(T)), list(T.keys()))
plt.xlabel('Time span (eg : 0 = 0000 to 0100hrs)')
plt.ylabel('Frequency of crime')
plt.show()