with open("Values.txt", "r") as f:
    r = f.readlines()

print ('Results are')
for i in r:
    x = i.split()
    fizz = int(x[0])
    buzz = int(x[1])
    n = int(x[2])
    print ("==================================")
    for j in range(1, n+1):
        if (j % fizz == 0) and (j % buzz == 0):
            print ('FB')
        elif (j % fizz == 0):
            print ('F')
        elif (j % buzz == 0):
            print ('B')
        else:
            print (j)
    