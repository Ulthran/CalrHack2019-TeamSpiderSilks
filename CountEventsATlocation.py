#HackCarleton
#13 April, 2019
# Bat-Orgil Batjargal\
 

import pandas as pd 
df = pd.read_csv("C:/Users/bator/Desktop/HackCarleton/Book.csv") 
#print (df) 
locations = {}
for row in df.itertuples():
#    print(row[5]) #string
    Value = row[5].casefold()
    try: 
        locations[Value] = locations[Value] + 1 
    except:
        locations[Value]=1
 
print (locations)

    



    