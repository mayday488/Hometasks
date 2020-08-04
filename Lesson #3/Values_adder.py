f = open ("A:\Python_Hometasks\Lesson #3\Values1.txt", "r+")
r = f.readlines()
print (r)
desired_number = 20
expected_number = 0
for i in r:
    x = i.split()
    x1 = int(x[0])
    x2 = int(x[1])
    x3 = int(x[2])
    print (i)
    f.write ('\n ========================= \n') 
    while desired_number != expected_number:
        n1 = x1 + 1
        f.write (str(n1)+ " ")
        n2 = x2 + 1
        f.write  (str(n2)+ " ")
        n3 = x3 + 1
        f.write  (str(n3)+ " ")
        f.write ('\n ========================= \n') 
        expected_number += 1
        x1 +=1
        x2 +=1
        x3 +=1
        
print ("Finished")
f.close()