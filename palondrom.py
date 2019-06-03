def palindrom(string):
    i=0
    while i<len(string):
        if string[i]==(string[-i-1]):
            result = True
        else:
            result = False
            break
        i+=1
    return result
print palindrom("momomomom")