# scrapeIndividualPage.py
#
# Team Spider Silks
# Author: Charlie Bushman
#
# Takes in the URL for an indiviudal event page and then scrapes the following
# data fields:
# Start Time, End Time, Location, From Site, Description, Category, For
#
# Takes in arguments of the URL to be scraped and then the name of the event
# and then the date of the event

import urllib.request
import re
import sys

# Reads in html
params = sys.argv[1].split("***")
url = params[0]
fp = urllib.request.urlopen(url)
byteStr = fp.read()

htmlStr = byteStr.decode("utf8")
fp.close()

# RegEx to find start and end times
# Preceeding string is:
# <span class="time">
# and following is:
# </span> <span class="divider">/</span>

searches = re.findall("<span class=\"time\">.+</span> <span class=\"divider\">/</span>", htmlStr)
startTime = "00:00:00"
endTime = "00:00:00"

if "8211" not in searches[0]:
  startTime = re.sub("<span class=\"time\">", "", searches[0])
  startTime = re.sub("</span> <span class=\"divider\">/</span>", "", startTime)
  endTime = ""
else:
  startTime = re.sub("<span class=\"time\">", "", searches[0])
  startTime = re.sub("</span> <span class=\"divider\">/</span>", "", startTime)
  endTime = re.sub(".+ &#8211; ", "", startTime)
  startTime = re.sub(" &#8211; .*", "", startTime)
  
  # Implement this please
  #print (int(startTime[0:1])+12)
  #if "am" not in endTime:
    #print (startTime[0:2])

# RegEx to find location
# Preceeding string is:
# <span class="divider">/</span> <span class="location">
# and following string is:
# </span></div>

searches = re.findall("<span class=\"divider\">/</span> <span class=\"location\">.+</span></div>", htmlStr)
location = "Nowhere"
for search in searches:
  location = re.sub("<span class=\"divider\">/</span> <span class=\"location\">", "", search)
  location = re.sub("</span></div>", "", location)

# RegEx to find description
# Preceeding string is:
# <p class="description">
# and following string is:
# </p>

searches = re.findall("<p class=\"description\">.+</p>", htmlStr)
description = "Boring"
for search in searches:
  description = re.sub("<p class=\"description\">", "", search)
  description = re.sub("</p>", "", description)

# RegEx to find the For field
# Preceeding string is:
# </div><div class="audiences"><h4>For:</h4>
# and the following line is:
# </div><div class="export">


# Export data into a .txt file
name = params[1]
date = params[2]
with open('allData' + date + '.txt', 'a+') as f:
  f.write(name + ", " + date + ", " + url + ", " + startTime + ", " + endTime + ", " + location + ", " + description)

