import plotly
import plotly.plotly as py
import pandas as pd
import xlrd
import plotly.graph_objs as go


'''
Cole's plots every category quantity over time

Mine: Checks to see if same location at same time.
- Raises warnings if they are very similar
- Raises alert if they are the same.

Example locations

Olin 149
Waverly, Iowa - Prairie Links Golf Course
Larson Meeting Room (WCC236)
Weitz Cinema
Building name
Room name
Leighton #305
TBD

Runs through year and saves location of each new event in a new list, along with it's id?
If the location matches a list already made, then it checks the times of the two IDs, and reports if they match
Doesn't leave wiggle room in location names


'''

# Create random data with numpy
import numpy as np

plotly.tools.set_credentials_file(username="CaptainCrouton89", api_key="QpQSb4FSQnuzS0q5DOSS")

calendarEventsDF = pd.read_excel("yearData.xlsx", skiprows = 0)

"""
Takes in start and end times and returns list of all numbers between those times
"""
def findHours(startTime, endTime):
    return [i for i in range(int(startTime.strip("0").strip(":")), int(endTime.strip("0").strip(":"))+1)]

print(findHours("03:00", "11:00"))

for index, row in calendarEventsDF.itterows()
    

'''
N = 500
random_x = np.linspace(0, 1, N)
random_y = np.random.randn(N)

# Create a trace
trace = go.Scatter(
    x = random_x,
    y = random_y
)

data = [trace]

py.plot(data, filename='basic')
'''
