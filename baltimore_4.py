import datetime
import xlrd 
import matplotlib.pyplot as plt
import gmplot 

loc = ("baltimore_crimes.xlsx")   
wb = xlrd.open_workbook(loc) 
sheet = wb.sheet_by_index(0)
C={}
T={}
T2={}

latitude_list = [] 
longitude_list = [] 

gmap1 = gmplot.GoogleMapPlotter(39.2846854,-76.6905261, 12 ) 

for i in range(24):
	i=str(i)
	T2[i]=0

for i in range(sheet.nrows - 1): 
	crime = sheet.cell_value(i+1,4)
	if crime=="LARCENY":
		y, m, d, h2, i, s = xlrd.xldate_as_tuple(sheet.cell_value(i+1,1), wb.datemode)
		t = str(h2)
		T2[t]+=1
		coordinate = sheet.cell_value(i+1,9)
		coordinate = coordinate.replace('(','').replace(')','')
		coordinate = coordinate.split(',')
		latitude_list.append(float(coordinate[0]))
		longitude_list.append(float(coordinate[1]))

gmap1.heatmap( latitude_list, longitude_list)
gmap1.draw( "map.html" ) 


for i in range(24):
	i=str(i)
	T[i]=0

for k in range(sheet.nrows - 1): 
	y, m, d, h, i, s = xlrd.xldate_as_tuple(sheet.cell_value(k+1,1), wb.datemode)
	t = str(h)
	T[t]+=1

for i in range(sheet.nrows - 1): 
	crime = sheet.cell_value(i+1,4)
	if crime in C :
		C[crime]+=1
	else:
		C[crime]=1

print(C)
plt.bar(range(len(C)), list(C.values()), align='center')
plt.xticks(range(len(C)), list(C.keys()))
plt.xticks(rotation=90)
plt.xlabel('Crime type')
plt.ylabel('Frequency of crime')
plt.show()


print(T2)
plt.bar(range(len(T2)), list(T2.values()), align='center')
plt.xticks(range(len(T2)), list(T2.keys()))
plt.xlabel('Time span (eg : 0 = 0000 to 0100hrs)')
plt.ylabel('Frequency of "LARCENY" crime')
plt.show()

x=[]
y={}
count=0
for i in T:
	x.append(i)
	
for j in C:
	y[j]=[]
	for k in T:
		for p in range(sheet.nrows - 1): 
			w, m, d, h, i ,s = xlrd.xldate_as_tuple(sheet.cell_value(p+1,1), wb.datemode)
			t = str(h)
			crime = sheet.cell_value(p+1,4)
			if str(k)==t and crime == j:
				count+=1 
		y[j].append(count)
		count=0

	plt.plot(x, y[j], label=j)	
	plt.legend()
print(y)
plt.xlabel('Time span (eg : 0 = 0000 to 0100hrs)')
plt.ylabel('Frequency of crime')
plt.show()