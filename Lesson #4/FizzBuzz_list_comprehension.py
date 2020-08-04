#FizzBuzz task using list comprehension:
n1 = int(input("Please enter the first number: "))
n2 = int(input("Please enter the second number: "))
n3 = int(input("Please enter the third number: "))
numbers = range(1,n3)
print ("=========================")
results = []
results = ["FB" if (i % n1 == 0) and (i % n2 == 0) else "F" if i % n1 == 0 else "B" if i % n2 == 0 
else i for i in range (1, n3+1)]
print ("Here is your results" + "\n=========================\n ")
print (results)

