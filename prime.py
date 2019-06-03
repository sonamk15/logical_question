def prime(x,y):
    prime_no=[]
    j=x+1
    while j<y:
        i=2
        while i<j:
            if j%i==0:
                print (False)
                break
            i+=1
        else:
            prime_no.append(j)
        j+=1
    return prime_no
print (prime(5,20))
