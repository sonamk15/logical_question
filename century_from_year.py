def centuryFromYear(year):
    if (year <= 0) :
        cout ="0 and negative is not allow for a year"
              
    elif (year <= 100) :
        
        cout= 1
         
    elif (year % 100 == 0) :
        cout = year/ 100  
    else:
        cout = year/ 100 + 1
    return cout
print centuryFromYear(2000)