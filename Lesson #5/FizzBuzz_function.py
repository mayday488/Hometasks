def FizzBuzz (n1,n2,n3):
    
    print ("----------------Results----------------") 

    for i in range(1, n3+1):
        if (i % n1 == 0) and (i % n2 == 0):
            print ("FB")
        elif (i % n1 == 0):
            print ('F')
        elif (i % n2 == 0):
            print ('B')
        else:
            print (i)
    return (i)

FizzBuzz(2, 5, 18)