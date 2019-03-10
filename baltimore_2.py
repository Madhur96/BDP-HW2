import datetime
import xlrd 
import matplotlib.pyplot as plt
from mapsplotlib import mapsplot as mplt
import gmplot 

loc = ("baltimore_crimes.xlsx")   
wb = xlrd.open_workbook(loc) 
sheet = wb.sheet_by_index(0)

latitude_list = [] 
longitude_list = [] 

gmap1 = gmplot.GoogleMapPlotter(39.2846854,-76.6905261, 12 ) 

for i in range(sheet.nrows - 1): 
	coordinate = sheet.cell_value(i+1,9)
	coordinate = coordinate.replace('(','').replace(')','')
	coordinate = coordinate.split(',')
	latitude_list.append(float(coordinate[0]))
	longitude_list.append(float(coordinate[1]))

gmap1.heatmap( latitude_list, longitude_list)
gmap1.draw( "map.html" ) 