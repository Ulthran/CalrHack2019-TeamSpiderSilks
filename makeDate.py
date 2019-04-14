# makeDate.py
#
# Team SpiderSilks
# Author: Charlie Bushman
#
# Runs scrapeMain on range of dates given here

import sys
import datetime
import scrapeMainCalendar

year = "2019"
month = "04"

for i in range(1, 30):
  rawDate = year + "-" + month + "-" + str(i)
  date = datetime.datetime.strptime(rawDate, '%Y-%m-%d')
  
  scrapeMainCalendar.main(str(date)[0:10])

