n1 = (int(input()))
n2 = (int(input()))
n3 = (int(input()))

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