import pandas as pd
import xlrd
import plotly
import plotly.plotly as py
import plotly.graph_objs as go
plotly.tools.set_credentials_file(username='colejump', api_key='Mh3sATfsUKQtelXlZTNP')

df = pd.read_excel("yearData.xls")

#counts the number of events for each day
numberCategoryPerDay = {}
numberPerDay = {}
xValues = []
yValues = []
categoryXValues = []
categoryYValues = []
count = 0
for index, row in df.iterrows():
	count = count + 1
for i in range(count):
	if (df.iloc[i][1]) in numberPerDay:
		numberPerDay[(df.iloc[i][2])] = numberPerDay[(df.iloc[i][2])] + 1
	else: 
		numberPerDay[(df.iloc[i][2])] = 1
	categoryList = df.iloc[i][9].split("; ")
	for x in categoryList:
		if (x) in numberCategoryPerDay:
			if (df.iloc[i][1]) in numberCategoryPerDay[x]:
				numberCategoryPerDay[x][(df.iloc[i][2])] = numberCategoryPerDay[x][(df.iloc[i][2])] + 1
			else: 
				numberCategoryPerDay[x][(df.iloc[i][2])] = 1	
			continue
		numberCategoryPerDay[x] = {df.iloc[i][2] : 1}
					
for x, y in numberPerDay.items():
	xValues.append(x)
	yValues.append(y)
trace = go.Scatter(
    x = xValues,
    y = yValues,
    name = 'Events',
    line = dict(
        color = ('rgb(0, 0, 0)'),
        width = 2)
)

data = [trace]

count = 0
tmpDic = {}
for i in numberCategoryPerDay:
	for k in numberPerDay:
		if k in numberCategoryPerDay[i]:
			tmpDic[k] = numberCategoryPerDay[i][k]
			continue
		else: 
			tmpDic[k] = 0
	red = str(int(count * (255/len(numberCategoryPerDay))))
	green = str(int(255 - (count * (255/len(numberCategoryPerDay)))))
	blue = str(int((255/4) + (count * ((255/4)/len(numberCategoryPerDay)))))
	for x, y in tmpDic.items():
		categoryXValues.append(x)
		categoryYValues.append(y)
	trace = go.Scatter(
		x = categoryXValues,
		y = categoryYValues,
		name = i,
		line = dict(
			color = ('rgb(' + red + ', ' + green + ', ' + blue + ')'),
			width = 2)
	)
	data.append(trace)
	categoryXValues = []
	categoryYValues = []
	count = count + 1
	
	
layout = dict(title = 'Events over time',
			  xaxis = dict(title = 'Day'),
			  yaxis = dict(title = 'Number of Events'),
			  )
fig = dict(data=data, layout=layout)
py.iplot(fig, filename='styled-line')













