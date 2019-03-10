from matplotlib import pyplot as plt
from wordcloud import WordCloud, STOPWORDS
import xlrd 

loc = ("global_terrorism_database.xlsx")   
wb = xlrd.open_workbook(loc) 
sheet = wb.sheet_by_index(0)  
comment_words = ' '
stopwords = set(STOPWORDS) 
comment_word = ' '
stopword = set(STOPWORDS) 

for i in range(sheet.nrows - 1): 
	summary = sheet.cell_value(i+1,18)
	motive = sheet.cell_value(i+1,64)
	s=summary.split()
	m=motive.split()
	if len(s)==0:
		continue
	else:
		s=s[1:]
		comment_words+= ' '.join(s)
	if len(m)==0:
		continue
	else:
		m=m[1:]
		comment_word+= ' '.join(m)
  
wordcloud = WordCloud(width = 800, height = 800, background_color ='black', stopwords = stopwords, min_font_size = 10).generate(comment_words)
plt.figure(figsize = (8, 8), facecolor = None) 
plt.imshow(wordcloud) 
plt.axis("off") 
plt.tight_layout(pad = 0)   
plt.show()	

wordclouds = WordCloud(width = 800, height = 800, background_color ='black', stopwords = stopword, min_font_size = 10).generate(comment_word)
plt.figure(figsize = (8, 8), facecolor = None) 
plt.imshow(wordclouds) 
plt.axis("off") 
plt.tight_layout(pad = 0)   
plt.show()	
