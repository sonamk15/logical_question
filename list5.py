
list = [1,6,5,4,3,2,8,7,9]
i=0
while i <len(list):
    j=0
    while j < len(list)-1:
        if list[j] > list[j + 1]:
                list[j], list[j + 1] = list[j + 1], list[j]
        j=j+1
    i+=1
print (list)

new=[]
i=0
while i<len(list):
    if list.index(list[i])%2==0:
        new.insert(new[0],list[i])
    else:
         new.append(list[i])
    i+=1
print (new)
