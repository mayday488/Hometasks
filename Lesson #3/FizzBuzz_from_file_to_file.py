with open("Values.txt", "r") as f:
    r = f.readlines()

print ('Results are')
g = open ("Results.txt", "w")
g.write ("================================\n") 
for i in r:
    x = i.split()
    fizz = int(x[0])
    buzz = int(x[1])
    n = int(x[2])
    for j in range(1, n+1):
        if (j % fizz == 0) and (j % buzz == 0):
            g.write ('FB ')
        elif (j % fizz == 0):
            g.write ('F ')
        elif (j % buzz == 0):
            g.write ('B ' )
        else:
            g.write (str(j)+ (" "))
    g.write ("\n================================\n")
g.close()