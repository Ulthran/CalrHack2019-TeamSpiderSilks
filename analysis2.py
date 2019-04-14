import pandas as pd
import xlrd
import plotly
import plotly.plotly as py
import plotly.graph_objs as go
plotly.tools.set_credentials_file(username='colejump', api_key='Mh3sATfsUKQtelXlZTNP')

df = pd.read_excel("yearData.xls")

#counts the number of events for each day
totalDayEvents = {}
numberPerDay = {}
dayTemplate = {"1":0, "2":0, "3":0, "4":0, "5":0, "6":0, "7":0, "8":0, "9":0, "10":0, "11":0, "12":0, "13":0, "14":0, "15":0, "16":0, "17":0, "18":0, "19":0, "20":0, "21":0, "22":0, "23":0}
xValues = []
yValues = []

count = 0
for index, row in df.iterrows():
	count = count + 1
for i in range(count):
	if (str(df.iloc[i][1])) in numberPerDay:
		start = df.iloc[i][2]
		startList = str(start).split(":")
		startHour = startList[0]
		startHour = int(startHour)
		end = df.iloc[i][3]
		endList = str(end).split(":")
		endHour = endList[0]
		endHour = int(endHour)
		while (endHour != startHour and endHour >= 0):
			numberPerDay[str(endHour)] = numberPerDay[str(endHour)] + 1
			if (endHour == 0):
				numberPerDay[str(df.iloc[i][1])] = numberPerDay[str(df.iloc[i][1])] + 1
			endHour = endHour - 1
		if i == (count-1):
			currentDayList = str(df.iloc[i][1]).split(" ")
			currentDay = currentDayList[0]
			tmp = []
			for j in numberPerDay:
				tmp.append(j)
			for k in tmp:
				if (k == tmp[0]):
					numberPerDay.pop(str(k))
					continue
				if (k == str(df.iloc[i][1])):
					numberPerDay[k] = numberPerDay.pop(str(k))
					continue
				if (len(str(k)) == 1):
					newTime = currentDay + " 0" + str(k) + ":00:00"
				else:
					newTime = currentDay + " " + str(k) + ":00:00"
				numberPerDay[newTime] = numberPerDay.pop(k)
			totalDayEvents.update(numberPerDay)
			print(numberPerDay)
			numberPerDay = {}
	else: 
		currentDayList = str(df.iloc[i][1]).split(" ")
		currentDay = currentDayList[0]
		tmp = []
		for j in numberPerDay:
			tmp.append(j)
		for k in tmp:
			if (k == tmp[0]):
				numberPerDay.pop(str(k))
				continue
			if (k == str(df.iloc[i][1])):
				numberPerDay[k] = numberPerDay.pop(str(k))
				continue
			if (len(str(k)) == 1):
				newTime = currentDay + " 0" + str(k) + ":00:00"
			else:
				newTime = currentDay + " " + str(k) + ":00:00"
			numberPerDay[newTime] = numberPerDay.pop(k)
		totalDayEvents.update(numberPerDay)
		print(numberPerDay)
		numberPerDay = {}
		numberPerDay[str(df.iloc[i][1])] = 0
		numberPerDay.update(dayTemplate)
		start = df.iloc[i][2]
		startList = str(start).split(":")
		startHour = startList[0]
		startHour = int(startHour)
		end = df.iloc[i][3]
		endList = str(end).split(":")
		endHour = endList[0]
		endHour = int(endHour)
		while (endHour != startHour and endHour >= 0):
			numberPerDay[str(endHour)] = numberPerDay[str(endHour)] + 1
			if (endHour == 0):
				numberPerDay[str(df.iloc[i][1])] = numberPerDay[str(df.iloc[i][1])] + 1
			endHour = endHour - 1
		if i == (count-1):
			currentDayList = str(df.iloc[i][1]).split(" ")
			currentDay = currentDayList[0]
			tmp = []
			for j in numberPerDay:
				tmp.append(j)
			for k in tmp:
				if (k == str(df.iloc[i][1])):
					numberPerDay[k] = numberPerDay.pop(str(k))
					continue
				if (len(str(k)) == 1):
					newTime = currentDay + " 0" + str(k) + ":00:00"
				else:
					newTime = currentDay + " " + str(k) + ":00:00"
				numberPerDay[newTime] = numberPerDay.pop(k)
			totalDayEvents.update(numberPerDay)
			print(numberPerDay)
			numberPerDay = {}
			
for x, y in totalDayEvents.items():
	xValues.append(x)
	yValues.append(y)
trace = go.Scatter(
    x = xValues,
    y = yValues,
    name = 'Total Events',
    line = dict(
        color = ('rgb(0, 0, 0)'),
        width = 2)
)

data = [trace]
	
layout = dict(title = 'Events per Hour',
			  xaxis = dict(title = 'Time'),
			  yaxis = dict(title = 'Number of Events'),
			  )
fig = dict(data=data, layout=layout)
py.iplot(fig, filename='styled-line')
