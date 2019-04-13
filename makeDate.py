# makeDate.py
#
# Team SpiderSilks
# Author: Charlie Bushman
#
# Takes in three hyphen separated numbers (year-month-day) and creates a date
# of the form yyyy-mm-dd
# Stores date in date.txt

import sys
import datetime
import scrapeMainCalendar

year = "2019"
month = "04"

for i in range(1, 30):
  rawDate = year + "-" + month + "-" + str(i)
  date = datetime.datetime.strptime(rawDate, '%Y-%m-%d')
  
  print(date)
  scrapeMainCalendar.main(str(date))

