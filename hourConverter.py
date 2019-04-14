#HackCarleton
#13 April, 2019
# Bat-Orgil Batjargal
 
#x = "3:00PM" #15
#y = "13:00"  #13
#z = "1:00am" #13
#n = "9:00" #21

def my_function(hourInString):
    numberCollecter = ""
    letterCollecter = ""
    leftNumber = ""

    numbersAndCharacter = [":","0","1","2","3","4","5","6","7","8","9"]
    letters = ["a","m","p"]

    for i in hourInString.casefold():            
        if i in numbersAndCharacter:
            numberCollecter += i
        elif i in letters:
            letterCollecter += i

    if len(numberCollecter)==4:
        numberCollecter ="0" + numberCollecter

    if (letterCollecter == "pm"):
        leftNumber = numberCollecter[:2]
        updatedNumberCollecter = str(int(leftNumber)+12)+numberCollecter[-3:]
        return updatedNumberCollecter 
    else:
        return numberCollecter

        

#def main ():
#    answer = my_function(n)
#    print (answer)
#main()
