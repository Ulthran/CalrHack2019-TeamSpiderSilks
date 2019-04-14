# scrapeMainCalendar.py
#
# Team Spider Silks
# Author: Charlie Bushman
#
# Does a RegEx search of the main calendar page on a given date and gets the
# links to the individual events that day.
# Writes links into eventURLs.txt and writes the data we have at this point
# into data*DATE*.txt.
# First argument is the date we're looking at

import urllib.request
import re
import sys

# Function for scraping each URL found above
def scrapeIndUrl(url, name, date):
	fp = urllib.request.urlopen(url)
	byteStr = fp.read()

	htmlStr = byteStr.decode("utf8")
	fp.close()

	# RegEx to find start and end times
	# Preceeding string is:
	# <span class="time">
	# and following is:
	# </span> <span class="divider">/</span>

	searches = re.findall("<span class=\"time\">.+</span>", htmlStr)
	startTime = "00:00:00"
	endTime = "00:00:00"

	if "8211" not in searches[0]:
	  startTime = re.sub("<span class=\"time\">", "", searches[0])
	  startTime = re.sub("</span> <span class=\"divider\">/</span>", "", startTime)
	  endTime = startTime
	else:
	  startTime = re.sub("<span class=\"time\">", "", searches[0])
	  startTime = re.sub("</span> <span class=\"divider\">/</span>", "", startTime)
	  startTime = re.sub(" <span class=\"location\">.*</span>", "", startTime)
	  startTime = re.sub(" <span class=\"location\">.*", "", startTime)
	  startTime = re.sub("</span>", "", startTime)
	  endTime = re.sub(".+ &#8211; ", "", startTime)
	  startTime = re.sub(" &#8211; .*", "", startTime)
	  if "am" in endTime and "am" not in startTime:
	    startTime = startTime + " am"
	  elif "pm" not in startTime:
	    startTime = startTime + " pm"
	  
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
	name = name.replace(",", ";")
	date = date.replace(",", ";")
	url = url.replace(",", ";")
	startTime = startTime.replace(",", ";")
	endTime = endTime.replace(",", ";")
	location = location.replace(",", ";")
	description = description.replace(",", ";")
	with open('data/data' + date + '.txt', 'a+') as f:
	  f.write(name + ", " + date + ", " + url + ", " + startTime + ", " + endTime + ", " + location + ", " + description + "\n")

def main(sysargv1):
	# Reads in html
	dateArg = sysargv1
	calURL = "https://apps.carleton.edu/calendar/?start_date=" + dateArg + "&view=daily&no_search=1"
	fp = urllib.request.urlopen(calURL)
	byteStr = fp.read()

	htmlStr = byteStr.decode("utf8")
	fp.close()

	# RegEx to sort out event URLs and names
	# Looking for this string which preceeds each URL:
	# <li class="event hasTime"><a href="?view=daily&amp;start_date=2019-04-13&amp;
	# and finishes with:
	# </a>

	searches = re.findall("<li class=\"event hasTime\"><a href=\"\?view=daily&amp;start_date=" + re.escape(dateArg) + "&amp;.+</a>", htmlStr)
	urls = []
	eventIDs = []
	dates = []
	names = []
	for search in searches:
	  print(search)
	  newSearch = re.sub("<li class=\"event hasTime\"><a href=\"\?view=daily&amp;start_date=" + re.escape(dateArg) + "&amp;", "", search)
	  newSearch = re.sub("</a>", "", newSearch)
	  # URL can be composed from event_id and date
	  eventID = re.findall("event_id=.+&amp;", newSearch)
	  eventID = re.sub("event_id=", "", eventID[0])
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

	# Writes data we have at this point to file
	if(len(dates) == 0):
	  dates.append(dateArg)
	i = 0
	open('data/data' + dates[0] + '.txt', 'w').close()
	for name in names:
	  print(urls[i] + " " + name + " " + dates[i])
	  scrapeIndUrl(urls[i], name, dates[i])
	  i += 1

if __name__ == "__main__":
	main(sys.argv[1])

