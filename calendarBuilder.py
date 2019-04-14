"""
calendarBuilder.py

*******************************************************************
IMPORTANT: WILL CLEAR ALL EVENTS ON WHATEVER CALENDAR IT IS USED ON
*******************************************************************


Author: Silas Rhyneer

Imports calendar data from an excel sheet and exports it to user's choice of
google calendars. It wipes the calendar, and then uploads all of the excel sheet.
"""

from __future__ import print_function
import datetime
import pickle
import os.path
import pandas as pd
import xlrd
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request

# If modifying these scopes, delete the file token.pickle.
SCOPES = ['https://www.googleapis.com/auth/calendar']

athleteActivities = ["Athletics Event"]
recActivities = ["Dance"]
infoActivities = ["Lecture"]

def categoryColor(category):
    if category in athleteActivities:
        colorId = 2
    elif category in recActivities:
        colorId = 5
    elif category in infoActivities:
        colorId = 9
    else:
        colorId = 3
    return colorId

def insertYearEvents(service, creds, name, location, description, date, startTime, endTime, category, link):
    event = {
      'summary': name,
      'location': location,
      'description': 'A chance to hear more about Google\'s developer products.',
      'start': {
        'dateTime': date + 'T' + startTime + ":00",
        'timeZone': 'America/Chicago',
      },
      'end': {
        'dateTime': date + 'T' + endTime + ":00",
        'timeZone': 'America/Chicago',
      },
      'description': str(category) + "\n" + str(description) + "\n\n" + str(link),
      'locked': True,
      'colorId': categoryColor(category),
      #'colorId': {
    #"background": "orange",
#        "foreground": 'yellow'
     # }
    }

    event = service.events().insert(calendarId='primary', body=event).execute()
    print('Event created: %s' % (event.get('htmlLink')))

def main():

    calendarEventsDF = pd.read_excel("dummyData.xls", skiprows = 0)

    creds = None
    # The file token.pickle stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server()
        # Save the credentials for the next run
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)

    service = build('calendar', 'v3', credentials=creds)

    service.calendars().clear(calendarId='primary').execute()

    for index, row in calendarEventsDF.iterrows():
        insertYearEvents(service, creds, row['name'], row['location'], row['description'], row['date'], row['startTime'], row['endTime'], row['category'], row['link'])



if __name__ == '__main__':
    main()
