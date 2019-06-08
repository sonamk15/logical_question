def adjacentElementsProduct(array):
    num=-100
    i=0
    while i<len(array)-1:
        if array[i]*array[i+1]>=num:
            num=array[i]*array[i+1]
        i+=1
    return num
print (adjacentElementsProduct([5, 1, 2, 3, 1, 4]))

