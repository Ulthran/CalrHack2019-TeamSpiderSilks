#!/bin/bash
#
# Team Spider Silks
# Author: Charlie Bushman
#
# Script to run the scraping functions for a single day of the campus calendar
# on many days

for i in {1..30..1}
  do
    python makeDate.py 2019-4-$i
    
    dateFile="date.txt"
    while IFS='' read -r line || [[ -n "$line" ]]; do
      echo $line1
      echo python scrapeMainCalendar.py "$line1"
    done < "$dateFile"
done
