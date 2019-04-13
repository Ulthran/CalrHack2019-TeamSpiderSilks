# scrapeMainCalendar.py
#
# Team Spider Silks
# Author: Charlie Bushman
#
# Does a RegEx search of the main calendar page on a given date and gets the
# links to the individual events that day.
# Writes links into eventURLs.txt and writes the data we have at this point
# into data*DATE*.txt.

import urllib.request
import re

# Reads in html
fp = urllib.request.urlopen("https://apps.carleton.edu/calendar/")
byteStr = fp.read()

htmlStr = byteStr.decode("utf8")
fp.close()

# RegEx to sort out event URLs and names
# Looking for this string which preceeds each URL:
# <li class="event hasTime"><a href="
# and finishes with:
# </a>

searches = re.findall("<li class=\"event hasTime\"><a href=\".+</a>", htmlStr)
urls = []
eventIDs = []
dates = []
names = []
for search in searches:
  newSearch = re.sub("<li class=\"event hasTime\"><a href=\"", "", search)
  newSearch = re.sub("</a>", "", newSearch)
  # URL can be composed from event_id and date
  eventID = re.findall("\?event_id=.+&amp;", newSearch)
  eventID = re.sub("\?event_id=", "", eventID[0])
  eventID = re.sub("&amp;", "", eventID)
  eventIDs.append(eventID)
  date = re.findall("&amp;.+\">", newSearch)
  date = re.sub("&amp;date=", "", date[0])
  date = re.sub("\">", "", date)
  dates.append(date)
  # Construct URL
  url = "https://apps.carleton.edu/calendar/?view=daily&start_date=" + date
  url = url + "&event_id=" + eventID + "&date=" + date
  urls.append(url)
  # Get event names as well
  name = re.findall("\">.+", newSearch)
  name = re.sub("\">", "", name[0])
  names.append(name)

# Writes urls to file eventURLs.txt
with open('eventURLs.txt', 'w') as f:
  for url in urls:
    f.write("%s\n" % url)

# Writes data we have at this point to data.txt
with open('data' + dates[0] + '.txt', 'w') as f:
  f.write("Name, Date, URL")
  i = 0
  for name in names:
    f.write("\n" +  name + ", " + dates[i] + ", " + urls[i])
    i += 1
